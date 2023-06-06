import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow
} from '@mui/material';
import React from 'react';

import { useEffect, useState } from 'react';
import api from '../services/api';
import { Container, HeadTableCell } from '../style/tableStyle';

const Comissions = () => {
  const [commissions, setComissions] = useState([]);
  
  useEffect(() => {
    const url = "api/commission_report/04-06-2023/06-06-2023/";
    api.get(url).then(({ data }) => {
      setComissions(data.data);
    })
  }, []);

  return (
    <Container>
        <h3>Relatório de Comissões</h3>
        <Table stickyHeader aria-label='simple table'>
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
