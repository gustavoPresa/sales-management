import React from 'react';
import { AngleRight, Container, InternalLink } from './styles';

const SidebarItem = ({ Icon, Text, Page }) => {
  return (
    <InternalLink to={Page}>
      <Container>
          <Icon />
          {Text}
          <AngleRight />
      </Container>
    </InternalLink>
  )
}

export default SidebarItem