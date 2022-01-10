import React from 'react'
import { Helmet } from 'react-helmet';
import { Box, Container, Grid } from '@material-ui/core';
import { Budget, LatestOrders, LatestSales, TotalCustomers, TotalProfit, TrafficByDevice, TotalProfit2, Navigation } from 'features/adminCommon'
import AppAppBar from '../layout/AppAppBar';
import 'features/adminCommon/components/grid.css'

export default function Dashboard() {
  return (
    <>
      <AppAppBar />
      <Helmet>
        <title>Dashboard | TripN Admin</title>
      </Helmet>
      <div className='container' >
        <Navigation />
        <Container maxWidth={false} className='item1' >
          <Grid
            container
            spacing={1}
          >
            <Grid
              item
              lg={3}
              sm={6}
              xl={3}
              xs={12}
            >
              <Budget />
            </Grid>
            <Grid
              item
              lg={3}
              sm={6}
              xl={3}
              xs={12}
            >
              <TotalProfit2 />
            </Grid>
            <Grid
              item
              lg={3}
              sm={6}
              xl={3}
              xs={12}
            >
              <TotalCustomers />
            </Grid>
            <Grid
              item
              lg={3}
              sm={6}
              xl={3}
              xs={12}
            >
              <TotalProfit sx={{ height: '100%' }} />
            </Grid>
            <Grid
              item
              lg={8}
              md={12}
              xl={9}
              xs={12}
            >
              <LatestSales />
            </Grid>
            <Grid
              item
              lg={4}
              md={6}
              xl={3}
              xs={12}
            >
              <TrafficByDevice sx={{ height: '100%' }} />
            </Grid>
            <Grid
              item
              lg={12}
              md={18}
              xl={12}
              xs={24}
            >
              <LatestOrders />
            </Grid>
          </Grid>
        </Container>
      </div>
    </>
  );
}