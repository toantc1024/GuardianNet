import React from 'react';
import { Coin, Setting2 } from 'iconsax-react';
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
    </div>
  );
};

import { ArrowDownOutlined, ArrowUpOutlined } from '@ant-design/icons';
import { Button, Card, Col, Row, Statistic } from 'antd';
const Stats = () => <div className="h-full w-full px-4 bg-red-400">HE</div>;

import { Carousel } from 'antd';
const contentStyle = {
  margin: 0,
  height: '300px',
  color: '#fff',
  lineHeight: '300px',
  textAlign: 'center',
};
const DashboardCaroseul = () => {
  return (
    <div className="p-2 flex gap-2 flex-col">
      <Card bordered={false}>
        <Statistic
          title="Active"
          value={11.28}
          precision={2}
          valueStyle={{ color: '#3f8600' }}
          prefix={<Coin />}
          suffix="netCoin"
        />
      </Card>
      <Button>Widthdraw now</Button>
    </div>
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
