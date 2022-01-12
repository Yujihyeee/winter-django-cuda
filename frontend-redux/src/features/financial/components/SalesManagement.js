import React from 'react'
import { Navigation, AppAppBar } from 'features/adminCommon'
import styled from 'styled-components'
import { Chart1, Chart2, Chart3, Chart4, ChartData1, ChartData2, ChartData3, ChartData4 } from 'features/financial'

export default function SalesManagement() {
    return (<>
        <AppAppBar />
        <div className='container' >
            <Navigation />
            <ChartTable>
                <Charttr>
                    <Charttd>
                        <h3>항목별 상세 매출</h3>
                        <Chartdiv><Chart2 data={ChartData2} /></Chartdiv>
                    </Charttd>
                    <Charttd rowSpan={2}>
                        <h3>MBTI</h3>
                        <Chartdiv><Chart3 data={ChartData3} /></Chartdiv>
                    </Charttd>
                </Charttr>
                <Charttr>
                    <Charttd>
                        <h3>6개월 매출</h3>
                        <Chartdiv><Chart1 data={ChartData1} /></Chartdiv>
                    </Charttd>
                </Charttr>
                <Charttr>
                    <Charttd colSpan='2'>
                        <h3>연간 이익</h3>
                        <Chartdiv><Chart4 data={ChartData4} /></Chartdiv>
                    </Charttd>
                </Charttr>
            </ChartTable>
        </div>
    </>)
}

const ChartTable = styled.table`
    width: 98%;
    height:700px;
`

const Charttr = styled.tr`
    width:100%;
    height:100%;
    margin:auto;
`

const Charttd = styled.td`
    margin:auto;
    padding:1%;
`

const Chartdiv = styled.div`
    display:block;
    margin:auto;
    width:840px;
    height:390px;
`