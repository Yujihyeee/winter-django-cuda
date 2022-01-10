import React from 'react'
import { Link } from 'react-router-dom'
import styled from 'styled-components';

const Navigation = () => (
    <>
    <Nav>
        <NavList>
            <NavItem><Link to = '/an/dash-board'>DashBoard</Link></NavItem>
            <NavItem><Link to = '/an/user-list'>UserList</Link></NavItem>
            <NavItem><Link to = '/an/sales-management'>SalesManagement</Link></NavItem>
            <NavItem><Link to = '/an/financial-reports'>FinancialReports</Link></NavItem>
        </NavList>
    </Nav>
    </>
)

export default Navigation;

const Nav = styled.div`
    text-align: center;
    padding:2%;
`

const NavList = styled.ul`
    width: 100%;

`

const NavItem = styled.li`
    line-height:60px;
    

`