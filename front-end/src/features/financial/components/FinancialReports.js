import React from 'react'
import styled from 'styled-components'
import { AppAppBar, Navigation } from 'features/adminCommon'

const FinancialReports = () => {
    return (<>
        <AppAppBar />
        <div className='container' >
            <Navigation className='navi' />
            <Table>
                <Tr>
                    TripN 손익계산서
                </Tr>
                <Tr>
                    <Td>항목</Td>
                    <Td>당기</Td>
                    <Td>전기</Td>
                    <Td>전전기</Td>
                </Tr>
                <Tr>
                    <Td>매출액</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>매출원가</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>판매비와관리비</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>지급수수료</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>영업이익</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>기타손익 및 금융손익</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>기타수익</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>기타비용</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>금융수익</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>금융비용</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>당기순이익</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
            </Table>
        </div>
    </>)
}

export default FinancialReports

const Table = styled.table`
    height:100%;
    margin: 1%;
`

const Tr = styled.tr`
    text-align:center;
`
const Td = styled.td`
    height:50px;
    width:100px;
    border: 1px solid black;
`