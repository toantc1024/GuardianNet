import React from 'react';

import {
  WEB_FILTERING_PAGE,
  LOCATION_PAGE,
  CHILDREN_PAGE,
  DASHBOARD_PAGE,
} from '../../../constants/popup_page';
import { Home, Book, User } from 'iconsax-react';
const IconButton = ({ icon, onClickHandler, isActive, activeIcon }) => {
  return (
    <div
      onClick={() => onClickHandler()}
      className="p-2  cursor-pointer text-2xl"
    >
      {isActive ? activeIcon : icon}{' '}
    </div>
  );
};
const BottomNavbar = ({ page, setPage }) => {
  return (
    <div className="flex py-4 items-center justify-between px-16">
      <IconButton
        onClickHandler={() => setPage(DASHBOARD_PAGE)}
        icon={
          <Home
            size="32"
            className="text-gray-400 hover:text-gray-300 transition-text ease-in-out-duration-150"
            variant="Bold"
          />
        }
        isActive={page === DASHBOARD_PAGE}
        activeIcon={
          <Home size="32" className="text-violet-400" variant="Bold" />
        }
      />
      <IconButton
        onClickHandler={() => setPage(LOCATION_PAGE)}
        icon={
          <Book
            size="32"
            className="text-gray-400 hover:text-gray-300 transition-text ease-in-out-duration-150"
            variant="Bold"
          />
        }
        isActive={page === LOCATION_PAGE}
        activeIcon={
          <Book size="32" className="text-yellow-400" variant="Bold" />
        }
      />

      <IconButton
        onClickHandler={() => setPage(CHILDREN_PAGE)}
        icon={
          <User
            size="32"
            className="text-gray-400 hover:text-violet-200 transition-text ease-in-out-duration-150"
            variant="Bold"
          />
        }
        isActive={page == CHILDREN_PAGE}
        activeIcon={
          <User size="32" className="text-green-500" variant="Bold" />
        }
      />
      {/* 
      <IconButton
        onClickHandler={() => setPage(WEB_FILTERING_PAGE)}
        icon={<BsPlayFill className="text-gray-400" />}
        isActive={page == WEB_FILTERING_PAGE}
        activeIcon={<PlayCircle className="text-yellow-400" />}
      />
      <IconButton
        onClickHandler={() => setPage(LOCATION_PAGE)}
        icon={<BsHeartFill className="text-gray-400" />}
        isActive={page == LOCATION_PAGE}
        activeIcon={<BsHeartFill className="text-pink-400" />}
      />
      <IconButton
        icon={<BsPeopleFill className="text-gray-400" />}
        onClickHandler={() => setPage(CHILDREN_PAGE)}
        isActive={page == CHILDREN_PAGE}
        activeIcon={<BsPeopleFill className="text-green-600" />}
      /> */}
    </div>
  );
};

export default BottomNavbar;
