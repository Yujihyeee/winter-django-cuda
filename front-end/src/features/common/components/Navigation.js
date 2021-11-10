import React from 'react'
import { Link } from 'react-router-dom'
import styled from 'styled-components';

export default function Navigation() {
    return (
        <Nav>
            <NavList>
                <NavItem><Link to = '/home'>Home</Link></NavItem>
                <NavItem><Link to="/users/join">UserAdd</Link></NavItem>
                <NavItem><Link to="/users/detail">UserDetail</Link></NavItem>
                <NavItem><Link to="/users/list">UserList</Link></NavItem>
                <NavItem><Link to="/users/login">UserLogin</Link></NavItem>
                <NavItem><Link to="/users/modify">UserModify</Link></NavItem>
                <NavItem><Link to="/users/remove">UserRemove</Link></NavItem>
            </NavList>
        </Nav>
    )
}

const Nav = styled.div`
    width: 100%;
    height: 100px;
    border-bottom: 1px soild #d1d8e4;

`
const NavList = styled.ul`
    width: 1080px;
    display: flex;
    margin: 0 auto;
`

const NavItem = styled.li`
    width: auto;
    margin-left: 20px;
    margin-top: 30px;
    display: flex;
`