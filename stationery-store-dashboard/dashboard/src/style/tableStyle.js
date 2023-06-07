import { TableCell } from '@mui/material';
import styled from 'styled-components';

export const Container = styled.div`
  padding: 30px;

  > h3 {
    color: #14646c;
    margin-bottom: 15px;
  }
`;

export const DateFields = styled.div`
  float: right;
  margin-bottom: 15px;
`;

export const HeadTableCell = styled(TableCell)`
  position: inherit !important;
  font-weight: 900 !important;
`;