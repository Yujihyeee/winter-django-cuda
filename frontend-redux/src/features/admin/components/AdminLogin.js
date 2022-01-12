import React from 'react'
import { useNavigate } from 'react-router-dom';
import { Helmet } from 'react-helmet';
import * as Yup from 'yup';
import { Formik } from 'formik';
import { Box, Button, Container, Grid, TextField, Typography } from '@material-ui/core';

export default function AdminLogin() {
    const navigate = useNavigate();

    return (<>
        <Helmet>
            <title>TripN Admin</title>
        </Helmet>
        <Box
            sx={{
                backgroundColor: 'background.default',
                display: 'flex',
                flexDirection: 'column',
                height: '100%',
                justifyContent: 'center'
            }}
        >
            <Container maxWidth="sm">
                <Formik
                    initialValues={{
                        email: 'demo@tripn.shop',
                        password: 'Password123'
                    }}
                    validationSchema={Yup.object().shape({
                        email: Yup.string().email('Must be a valid email').max(55).required('Email is required'),
                        password: Yup.string().max(25).required('Password is required')
                    })}
                    onSubmit={() => {
                        navigate('/an/dash-board', { replace: true });
                    }}
                >
                    {({
                        errors,
                        handleBlur,
                        handleChange,
                        handleSubmit,
                        isSubmitting,
                        touched,
                        values
                    }) => (
                        <form onSubmit={handleSubmit}>
                            <Box sx={{ mb: 3 }}>
                                <Typography
                                    color="textPrimary"
                                    variant="h2"
                                >
                                    Admin Page
                                </Typography>
                                <Typography
                                    color="textSecondary"
                                    gutterBottom
                                    variant="body2"
                                >
                                    Sign in on the internal platform
                                </Typography>
                            </Box>
                            <Grid
                                container
                                spacing={3}
                            >
                                <Grid
                                    item
                                    xs={12}
                                    md={6}
                                >
                                </Grid>
                                <Grid
                                    item
                                    xs={12}
                                    md={6}
                                >
                                </Grid>
                            </Grid>
                            <Box
                                sx={{
                                    pb: 1,
                                    pt: 3
                                }}
                            >
                                <Typography
                                    align="center"
                                    color="textSecondary"
                                    variant="body1"
                                >
                                    Login with email address
                                </Typography>
                            </Box>
                            <TextField
                                error={Boolean(touched.email && errors.email)}
                                fullWidth
                                helperText={touched.email && errors.email}
                                label="Email Address"
                                margin="normal"
                                name="email"
                                onBlur={handleBlur}
                                onChange={handleChange}
                                type="email"
                                value={values.email}
                                variant="outlined"
                            />
                            <TextField
                                error={Boolean(touched.password && errors.password)}
                                fullWidth
                                helperText={touched.password && errors.password}
                                label="Password"
                                margin="normal"
                                name="password"
                                onBlur={handleBlur}
                                onChange={handleChange}
                                type="password"
                                value={values.password}
                                variant="outlined"
                            />
                            <Box sx={{ py: 2 }}>
                                <Button
                                    color="primary"
                                    disabled={isSubmitting}
                                    fullWidth
                                    size="large"
                                    type="submit"
                                    variant="contained"
                                >
                                    Sign in now
                                </Button>
                            </Box>
                        </form>
                    )}
                </Formik>
            </Container>
        </Box>
    </>);
};