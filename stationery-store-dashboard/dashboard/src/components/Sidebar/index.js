import React from 'react'
import {
  FaCalculator,
  FaCashRegister
} from 'react-icons/fa'
import { Container, Content } from './styles'

import SidebarItem from '../SidebarItem'

const Sidebar = ({ active }) => {
   return (
    <Container sidebar={active}>
      <Content>
        <SidebarItem Icon={FaCashRegister} Text="Vendas" Page="/vendas" />
        <SidebarItem Icon={FaCalculator} Text="Comissões" Page="/comissoes" />
      </Content>
    </Container>
  )
}

export default Sidebar