import React from 'react';
import { Route, Routes } from 'react-router-dom'
import { AdminLogin } from 'features/admin';
import { DashBoard } from 'features/adminCommon';
import { FinancialReports, SalesManagement } from 'features/financial';
import { UserList } from 'features/adminUser';


function App() {
  return (<>
    <div className="App">
         <Routes>
          {/* adminpage */}
          <Route path='/an' element={<AdminLogin />} />
          <Route path='/an/dash-board' element={<DashBoard />} />
          <Route path='/an/user-list' element={<UserList />} />
          <Route path='/an/sales-management' element={<SalesManagement />} />
          <Route path='/an/financial-reports' element={<FinancialReports />} />
        </Routes>
    </div>
  </>);
}

export default App;
