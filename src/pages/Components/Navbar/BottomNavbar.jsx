import React from 'react';

import {
  WEB_FILTERING_PAGE,
  LOCATION_PAGE,
  CHILDREN_PAGE,
  DASHBOARD_PAGE,
} from '../../../constants/popup_page';
import { BsHeartFill, BsPeopleFill, BsPlayFill } from 'react-icons/bs';
import { RiHeart2Fill, RiHome5Fill } from 'react-icons/ri';
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
        icon={<RiHome5Fill className="text-gray-400" />}
        isActive={page == DASHBOARD_PAGE}
        activeIcon={<RiHome5Fill className="text-violet-600" />}
      />

      <IconButton
        onClickHandler={() => setPage(WEB_FILTERING_PAGE)}
        icon={<BsPlayFill className="text-gray-400" />}
        isActive={page == WEB_FILTERING_PAGE}
        activeIcon={<BsPlayFill className="text-yellow-400" />}
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
      />
    </div>
  );
};

export default BottomNavbar;
