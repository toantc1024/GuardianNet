import React from 'react';
import { Setting2 } from 'iconsax-react';
const DashboardPageHeader = () => {
  return (
    <div className="w-full flex justify-between  p-4">
      <div className="flex justify-between gap-4 items-center">
        {/* Avatar */}
        <div className="w-10 h-10 rounded-full bg-red-900"></div>
        <div className="flex flex-col">
          <span className="font-bold text-2xl">Anne</span>
          <span>Active</span>
        </div>
      </div>

      <div className="flex items-center justify-center">
        <Setting2 className="text-4xl" />
      </div>
    </div>
  );
};

import { Carousel } from 'antd';
const contentStyle = {
  margin: 0,
  height: '300px',
  color: '#fff',
  lineHeight: '300px',
  textAlign: 'center',
};
const DashboardCaroseul = () => {
  const onChange = (currentSlide) => {
    console.log(currentSlide);
  };
  return (
    <Carousel afterChange={onChange}>
      <div>
        <h3 style={contentStyle}>
          <div className="p-8 pb-16">
            <div className="bg-red-500">Hello</div>
          </div>
        </h3>
      </div>
      <div>
        <h3 style={contentStyle}>4</h3>
      </div>
    </Carousel>
  );
};

const DashboardPage = () => {
  return (
    <>
      <DashboardPageHeader />
      <DashboardCaroseul />
    </>
  );
};

export default DashboardPage;
