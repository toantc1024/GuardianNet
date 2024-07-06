import React, { useState } from 'react';
import BottomNavbar from '../Components/Navbar/BottomNavbar';
import './Popup.css';
import DashboardPage from '../Components/PopupPages/DashboardPage';
import {
  WEB_FILTERING_PAGE,
  LOCATION_PAGE,
  CHILDREN_PAGE,
  DASHBOARD_PAGE,
} from '../../constants/popup_page';

const Popup = () => {
  const [currentPage, setCurrentPage] = useState(DASHBOARD_PAGE);
  return (
    <div className="h-screen w-full flex flex-col">
      <div className="h-full bg-sky-900">
        {currentPage == DASHBOARD_PAGE ? <DashboardPage /> : null}
      </div>
      <BottomNavbar
        page={currentPage}
        setPage={(value) => setCurrentPage(value)}
      />
    </div>
  );
};

export default Popup;
