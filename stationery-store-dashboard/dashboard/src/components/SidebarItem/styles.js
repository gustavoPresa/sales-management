import {
  FaAngleRight
} from 'react-icons/fa';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

export const Container = styled.div`
  display: flex;
  align-items: center;
  background-color: #fafafa; 
  font-size: 16px;
  font-weight: 700;
  color: #14646c;
  padding: 10px;
  cursor: pointer;
  margin: 0 0 5px;
  text-decoration: none !important;

  > svg {
    margin: 0 20px;
    font-size: 16px;
  }
}
`;

export const AngleRight  = styled(FaAngleRight)`
  right: 0px;
  position: absolute;
  color: #f0f0f0;
  font-size: 20px !important; 
`;

export const InternalLink  = styled(Link)`
  text-decoration: none !important;
`;