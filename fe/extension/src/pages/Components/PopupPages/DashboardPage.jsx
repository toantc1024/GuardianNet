import React, { useEffect, useState } from 'react';
import { Coin, Setting2 } from 'iconsax-react';
const DashboardPageHeader = ({ currentUser }) => {
  return (
    <div className="w-full flex justify-between  p-4">
      <div className="flex justify-between gap-4 items-center">
        {/* Avatar */}
        <div className="w-10 h-10 rounded-full bg-gradient-to-tr from-red-400 to-sky-500"></div>
        <div className="flex flex-col">
          <span className="font-bold text-2xl">{currentUser?.username}</span>
          <span className="text-green-500 font-bold">Active</span>
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
const DashboardCaroseul = ({ currentReward }) => {
  return (
    <div className="p-2 flex gap-2 flex-col">
      <Card bordered={false}>
        <Statistic
          title="Active"
          value={currentReward?.reward?.web_access || 0}
          precision={0}
          valueStyle={{ color: '#3f8600' }}
          prefix={<Coin />}
          suffix="rewards"
        />
      </Card>
      <Button
        onClick={() => {
          // Open new tab in browser
          window.open('http://localhost:3000/', '_blank');
        }}
      >
        Widthdraw now
      </Button>
    </div>
  );
};

const DashboardPage = ({ currentUser }) => {
  const [currentReward, setCurrentReward] = useState(0);
  useEffect(() => {
    fetch(
      'http://localhost:8000/api/guardiannet/reward/' + currentUser.user_id,
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      }
    )
      .then((response) => response.json())
      .then((data) => {
        setCurrentReward(data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }, []);

  return (
    <>
      <DashboardPageHeader currentUser={currentUser} />
      <DashboardCaroseul currentReward={currentReward} />
    </>
  );
};

export default DashboardPage;
