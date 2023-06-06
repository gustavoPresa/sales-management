import styled from 'styled-components';

export const Container = styled.div`
  background-color: #f0f0f0;
  box-shadow: 2px 0 5px -2px #d7d3d3;
  position: fixed;
  height: 100%;
  top: 105px;
  left: 0px;
  width: 300px;
  left: ${props => props.sidebar ? '0' : '-100%'};
  animation: showSidebar .4s;

  > svg {
    position: fixed;
    color: #14646c;
    width: 30px;
    height: 30px;
    margin-top: 32px;
    margin-left: 32px;
    cursor: pointer;
  }

  @keyframes showSidebar {
    from {
      opacity: 0;
      width: 0;
    }
    to {
      opacity: 1;
      width: 300px;
    }
  }
`;

export const Content = styled.div`
  margin-top: 20px;
`;