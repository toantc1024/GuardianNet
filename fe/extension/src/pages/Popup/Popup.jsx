import React, { useEffect, useState } from 'react';
import BottomNavbar from '../Components/Navbar/BottomNavbar';
import './Popup.css';
import DashboardPage from '../Components/PopupPages/DashboardPage';
import {
  WEB_FILTERING_PAGE,
  LOCATION_PAGE,
  CHILDREN_PAGE,
  DASHBOARD_PAGE,
} from '../../constants/popup_page';

import { Button, Checkbox, Form, Input } from 'antd';

const LoginForm = ({ onFinish, onFinishFailed }) => (
  <Form
    name="basic"
    labelCol={{
      span: 8,
    }}
    wrapperCol={{
      span: 16,
    }}
    style={{
      maxWidth: 600,
    }}
    initialValues={{
      remember: true,
    }}
    onFinish={onFinish}
    onFinishFailed={onFinishFailed}
    autoComplete="off"
  >
    <Form.Item
      label="Username"
      name="username"
      rules={[
        {
          required: true,
          message: 'Please input your username!',
        },
      ]}
    >
      <Input />
    </Form.Item>

    <Form.Item
      label="Password"
      name="password"
      rules={[
        {
          required: true,
          message: 'Please input your password!',
        },
      ]}
    >
      <Input.Password />
    </Form.Item>

    <Form.Item
      name="remember"
      valuePropName="checked"
      wrapperCol={{
        offset: 8,
        span: 16,
      }}
    >
      <Checkbox>Remember me</Checkbox>
    </Form.Item>

    <Form.Item
      wrapperCol={{
        offset: 8,
        span: 16,
      }}
    >
      <Button htmlType="submit">Login</Button>
    </Form.Item>
  </Form>
);

const Popup = () => {
  const [currentUser, setCurrentUser] = useState(null);
  const [currentPage, setCurrentPage] = useState(DASHBOARD_PAGE);
  useEffect(() => {
    chrome.storage.sync.get('currentUser', function (res) {
      if (res && res.currentUser) setCurrentUser(res.currentUser);
    });
  }, []);
  const onFinish = (values) => {
    let user = values;
    setCurrentUser(user);
    chrome.storage.sync.set({ currentUser: user });
  };
  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };
  return (
    <div className="h-screen w-full flex flex-col">
      {!currentUser ? (
        <div className="flex items-center justify-center h-full">
          <LoginForm onFinish={onFinish} onFinishFailed={onFinishFailed} />
        </div>
      ) : (
        <>
          <div className="h-full ">
            {currentPage == DASHBOARD_PAGE ? <DashboardPage /> : null}
          </div>
          <BottomNavbar
            page={currentPage}
            setPage={(value) => setCurrentPage(value)}
          />
        </>
      )}
    </div>
  );
};

export default Popup;
