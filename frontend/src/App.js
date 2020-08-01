import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <strong className="title-name">TD-LTE查询管理系统</strong>
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <body className="body_style">
        <div className="login_block">
          <form>
            <div className="style_table">
              <b className="font_style">用户名：</b>
              <input type="text" />
            </div>
            <div className="style_table">
              <b className="font_style">密 码：</b>
              <input type="text" />
            </div>
          </form>
          <button className="login_btn">登录</button>
          <button className="login_btn">注册</button>
        </div>
      </body>
    </div>
  );
}

export default App;
