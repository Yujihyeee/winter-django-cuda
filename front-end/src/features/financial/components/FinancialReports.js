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
                    <Chartth>손익계산서</Chartth>
                </Tr>
            </Table>
        </div>
    </>)
}

export default FinancialReports

const Table = styled.table`
    height:100%;
`

const Tr = styled.tr`
    height:100%;
`

const Chartth = styled.th`
    height:400px;
`