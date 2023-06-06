import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow
} from '@mui/material';
import React, { useEffect, useState } from 'react';
import api from '../services/api';
import { Container, HeadTableCell } from '../style/tableStyle';

const Sales = () => {
  const [sales, setSales] = useState([]);
  
  useEffect(() => {
    api.get("api/sales/").then(({ data }) => {
      setSales(data);
    })
  }, []);
  
  return (
    <Container>
        <h3>Vendas Realizadas</h3>
        <Table stickyHeader aria-label='simple table'>
            <TableHead>
                <TableRow>
                    <HeadTableCell>Notal Fiscal</HeadTableCell>
                    <HeadTableCell>Cliente</HeadTableCell>
                    <HeadTableCell>Vendedor</HeadTableCell>
                    <HeadTableCell>Data da Venda</HeadTableCell>
                    <HeadTableCell>Valor Total</HeadTableCell>
                    <HeadTableCell align='center'>Opções</HeadTableCell>
                </TableRow>
            </TableHead>
            <TableBody>
                {sales.map(row => (
                    <TableRow key={row.id}>
                        <TableCell>{row.invoice_number}</TableCell>
                        <TableCell>{row.client.name}</TableCell>
                        <TableCell>{row.seller.name}</TableCell>
                        <TableCell>{row.created_at}</TableCell>
                        <TableCell>R$ {row.amount}</TableCell>
                        <TableCell align='center'>-</TableCell>
                    </TableRow>
                ))}
            </TableBody>
        </Table>
    </Container>
  );
}

export default Sales
