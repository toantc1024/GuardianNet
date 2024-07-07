import React, { useEffect, useState } from 'react';
import BottomNavbar from '../Components/Navbar/BottomNavbar';
import './Popup.css';
import DashboardPage from '../Components/PopupPages/DashboardPage';
import LocationPage from '../Components/PopupPages/LocationPage';
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
  const onFinish = async (values) => {
    let user = values;
    fetch('http://localhost:8000/api/guardiannet/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: values.username,
        password: values.password,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data) {
          setCurrentUser(data);
          console.log('Success:', data);
          chrome.storage.sync.set({ currentUser: data });
        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });
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
          <div className="min-h-screen overflow-auto">
            {currentPage == DASHBOARD_PAGE ? (
              <DashboardPage currentUser={currentUser} />
            ) : currentPage === LOCATION_PAGE ? (
              <LocationPage currentUser={currentUser} />
            ) : null}
          </div>
          <BottomNavbar
            page={currentPage}
            logoutHandler={() => {
              setCurrentUser(null);
              chrome.storage.sync.remove('currentUser');
            }}
            setPage={(value) => setCurrentPage(value)}
          />
        </>
      )}
    </div>
  );
};

export default Popup;
