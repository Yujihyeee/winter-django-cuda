import React from 'react'
import styled from 'styled-components'
import { AppAppBar, Navigation } from 'features/adminCommon'

const FinancialReports = () => {
    return (<>
        <AppAppBar />
        <div className='container' >
            <Navigation className='navi' />
            <Table>
                <tr>
                    <td colSpan='5' style={{ textAlign: 'center' }}><h2>손익계산서</h2></td>
                </tr>
                <tr>
                    <td colSpan='5' style={{ textAlign: 'center' }}>당기 : 2021년 1월 1일부터 2021년 12월 31일까지</td>
                </tr>
                <tr>
                    <td colSpan='5' style={{ textAlign: 'center' }}>전기 : 2020년 1월 1일부터 2020년 12월 31일까지</td>
                </tr>
                <Tr>
                    <Td>항목</Td>
                    <Td colSpan='2'>당기금액</Td>
                    <Td colSpan='2'>전기금액</Td>
                </Tr>
                <Tr>
                    <Td>매출액</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>매출원가</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>판매비와관리비</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>지급수수료</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>영업이익</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>기타손익 및 금융손익</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>기타수익</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>기타비용</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>금융수익</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>금융비용</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                    <Td>0</Td>
                </Tr>
                <Tr>
                    <Td>당기순이익</Td>
                    <Td>0</Td>
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
    align:center;
    height:100%;
    width:90%;
    margin: 1%;
    margin-left:100px;
`

const Tr = styled.tr`
    text-align:center;
`
const Td = styled.td`
    height:40px;
    width:100px;
    border: 1px solid black;
`