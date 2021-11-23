import React from 'react'
import { Navigation, AppAppBar } from 'features/adminCommon'
import moment from 'moment';
import { v4 as uuid } from 'uuid';
import {
    Box,
    Card,
    CardHeader,
    Divider,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableRow
} from '@material-ui/core';

const orders = [
    {
        id: uuid(),
        ref: 'CDD1049',
        amount: 30.5,
        customer: {
            name: 'Ekaterina Tankova'
        },
        createdAt: 1555016400000,
        status: 'pending'
    },
    {
        id: uuid(),
        ref: 'CDD1048',
        amount: 25.1,
        customer: {
            name: 'Cao Yu'
        },
        createdAt: 1555016400000,
        status: 'delivered'
    },
    {
        id: uuid(),
        ref: 'CDD1047',
        amount: 10.99,
        customer: {
            name: 'Alexa Richardson'
        },
        createdAt: 1554930000000,
        status: 'refunded'
    }
];

const UserList = (props) => {
    return (<>
        <AppAppBar />
        <div className='container' >
            <Navigation />
            <Card {...props}>
                <CardHeader title="User List" align='center' />
                <Divider />
                <Box sx={{ minWidth: 800 }}>
                    <Table>
                        <TableHead>
                            <TableCell>
                                <label>이름:<input type="text" title="search" /></label><br /><br />
                                <label>생년월일:<input type="text" title="search" placeholder="No Hyphen" /></label><br /><br />
                                <label>휴대폰번호:<input type="tel" id="phone" pattern="[0-9]{3}-[0-9]{4}-[0-9]{4}" placeholder="No Hyphen" /></label>
                                <p><input type="submit" value="search" /></p>
                            </TableCell>
                        </TableHead>
                        <TableHead>
                            <TableRow>
                                <TableCell>
                                    이름
                                </TableCell>
                                <TableCell>
                                    ID
                                </TableCell>
                                <TableCell>
                                    생년월일
                                </TableCell>
                                <TableCell>
                                    전화번호
                                </TableCell>
                                <TableCell>
                                    최근예약날짜
                                </TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {orders.map((order) => (
                                <TableRow
                                    hover
                                    key={order.id}
                                >
                                    <TableCell>
                                        {order.ref}
                                    </TableCell>
                                    <TableCell>
                                        {order.customer.name}
                                    </TableCell>
                                    <TableCell>
                                        {moment(order.createdAt).format('DD/MM/YYYY')}
                                    </TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </Box>
            </Card>
        </div>
    </>)
}

export default UserList
