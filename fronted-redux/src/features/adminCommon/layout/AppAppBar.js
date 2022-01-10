import * as React from 'react';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import { AppBar, Toolbar } from 'features/adminCommon';

export default function AppAppBar() {
  return (
    <div>
      <AppBar position="fixed">
        <Toolbar sx={{ justifyContent: 'space-between', bgcolor: "#3c495e" }}>
          <Box sx={{ flex: 1 }} />
          <Link
            variant="h5"
            underline="none"
            color="inherit"
          >
            {'Trip N'}
          </Link>
          <Box sx={{ flex: 1, display: 'flex', justifyContent: 'flex-end' }}>
          </Box>
        </Toolbar>
      </AppBar>
      <Toolbar />
    </div>
  );
}
