import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  TextField
} from '@mui/material';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import moment from 'moment';
import React, { useEffect, useState } from 'react';
import api from '../services/api';
import { Container, DateFields, HeadTableCell } from '../style/tableStyle';

const Comissions = () => {
  const [commissions, setComissions] = useState([]);
  const [fromSelectedDate, setFromSelectedDate] = useState(null);
  const [toSelectedDate, setToSelectedDate] = useState(null);

  useEffect(() => {
    if (fromSelectedDate !== null && toSelectedDate !== null) {
      const fromDate = moment(fromSelectedDate.$d.toISOString()).format('DD-MM-YYYY');
      const toDate = moment(toSelectedDate.$d.toISOString()).format('DD-MM-YYYY');
      const url = `api/commission_report/${fromDate}/${toDate}`;
      
      api.get(url).then(({ data }) => {
        setComissions(data.data);
      })
    }
  }, [toSelectedDate, fromSelectedDate]);

  return (
    <Container>
        <DateFields>
          <LocalizationProvider dateAdapter={AdapterDayjs}>
            <DatePicker
              label="Período de Início"
              value={fromSelectedDate}
              format="DD-MM-YYYY"
              onChange={(newValue) => setFromSelectedDate(newValue)}
              renderInput={(props) => <TextField {...props} />}
            />
            <DatePicker
              label="Período de Fim"
              value={toSelectedDate}
              format="DD-MM-YYYY"
              onChange={(newValue) => setToSelectedDate(newValue)}
              renderInput={(props) => <TextField {...props} />}
            />
          </LocalizationProvider>
        </DateFields>
        <h3>Relatório de Comissões</h3>
        <Table>
            <TableHead>
                <TableRow>
                    <HeadTableCell>Cód.</HeadTableCell>
                    <HeadTableCell>Vendedor</HeadTableCell>
                    <HeadTableCell>Total de Vendas</HeadTableCell>
                    <HeadTableCell>Total de Comissões</HeadTableCell>
                </TableRow>
            </TableHead>
            <TableBody>
                {commissions.map(row => (
                    <TableRow key={row.id}>
                        <TableCell>{row.id}</TableCell>
                        <TableCell>{row.name}</TableCell>
                        <TableCell>{row.total_sales}</TableCell>
                        <TableCell>R$ {row.total_commission}</TableCell>
                    </TableRow>
                ))}
            </TableBody>
        </Table> 
    </Container>
  )
}

export default Comissions
