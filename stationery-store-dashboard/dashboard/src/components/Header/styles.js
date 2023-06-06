import styled from 'styled-components';

export const Container = styled.div`
  height: 100px;
  display: flex;
  background-color: #f0f0f0; 
  box-shadow: 0 0 8px 2px #bbbbbb;

  > svg {
    position: fixed;
    color: #14646c;
    width: 30px;
    height: 30px;
    margin-top: 32px;
    margin-left: 32px;
    cursor: pointer;
  }

  > h1 {
    position: fixed;
    right: 50%;
    margin-top: 25px;
  }
`;