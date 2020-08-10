import React from 'react';
import logo from './logo.svg';
import './App.css';

import axios from 'axios';
import {Redirect} from 'react-router-dom';

const ipaddr = 'http://127.0.0.1:8000/';

class LoginEnd extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            loginMode: true,
            username: '',
            password: '',
            first_name: '',
            last_name: '',
            email: '',
            password_comfirm: '',
            redirect: false
        };
        this.loginRequest = this.loginRequest.bind(this);
        this.registerRequest = this.registerRequest.bind(this);
    }

    loginRequest(){
        if(this.state.username === ''){
            alert('用户名为空, 请重新输入');
        }else if(this.state.password === ''){
            alert('密码为空，请重新输入');
        }else{
            axios.post(ipaddr + 'account/login/', {
                "login": this.state.username,
                "password": this.state.password
            }).then((response)=>{
                console.log('response: ' + response.data);
                if(response.data.detail != null && response.data.detail === "Login successful"){  // 登录成功
                    alert("登录成功");
                    this.setState({redirect: true});
                }else{
                    alert('账户不存在或密码输入有误');
                }
            }).catch((error)=>{
                var alt = '';
                for(var ky in error.response.data)
                    alt += (ky + ': ' + error.response.data[ky] + '\n');
                alert(alt);
            });
        }
    }

    registerRequest(){
        var data = {
            "username": this.state.username,
            "first_name": this.state.first_name,
            "last_name": this.state.last_name,
            "email": this.state.email,
            "password": this.state.password,
            "password_confirm": this.state.password_comfirm,
        };
        var path = ipaddr + 'account/register/';
        console.log("path: " + path + "\ndata: " + JSON.stringify(data));
        axios.post(ipaddr + 'account/register/', {
            "username": this.state.username,
            "first_name": this.state.first_name,
            "last_name": this.state.last_name,
            "email": this.state.email,
            "password": this.state.password,
            "password_confirm": this.state.password_comfirm,
        }, {
            headers: {
                "Content-Type": "application/json"
            }
        }).then((response)=>{
            if(response.data.id != null){
                alert('register successfully');
                this.setState({loginMode: true});
            }else{
                var alt = '';
                for(var ky in response.data)
                    alt += ky + ': ' +response.data[ky];
                alert('输入有误：' + alt);
            }
        }).catch((error)=>{
            var alt = '';
            for(var ky in error.response.data)
                alt += (ky + ': ' + error.response.data[ky] + '\n');
            alert(alt);
        });
    }

    render(){
        let content;
        if (this.state.loginMode){
            content = (
                <div>
                    <form>
                        <div className="style_table">
                            <b className="font_style">用户名：</b>
                            <input lassName="input_bar2" type="text" onChange={(e)=>this.setState({username: e.target.value})}/>
                        </div>
                        <div className="style_table">
                            <b className="font_style">密 码：</b>
                            <input className="input_bar2" style={{left: '0px'}} type="password" onChange={(e)=>this.setState({password: e.target.value})}/>
                        </div>
                    </form>
                    <button className="login_btn_now" onClick={this.loginRequest}>登录</button>
                    <button className="login_btn" onClick={()=>this.setState({loginMode: false})}>注册</button>
                </div>
            )
        }else{
            content = (
                <div>
                    <form>
                        <div className="style_table">
                            <b className="font_style">用户名：</b>
                            <input className="input_bar2" type="text" onChange={(e)=>this.setState({username: e.target.value})}/>
                        </div>
                        <div className="style_table">
                            <b className="font_style">姓 氏：</b>
                            <input className="input_bar2" type="text" onChange={(e)=>this.setState({first_name: e.target.value})}/>
                        </div>
                        <div className="style_table">
                            <b className="font_style">名 字：</b>
                            <input className="input_bar2" type="text" onChange={(e)=>this.setState({last_name: e.target.value})}/>
                        </div>
                        <div className="style_table">
                            <b className="font_style">邮 箱：</b>
                            <input className="input_bar2" type="text" onChange={(e)=>this.setState({email: e.target.value})}/>
                        </div>
                        <div className="style_table">
                            <b className="font_style">密 码：</b>
                            <input className="input_bar2" type="password" onChange={(e)=>this.setState({password: e.target.value})}/>
                        </div>
                        <div className="style_table">
                            <b className="font_style">密码确认：</b>
                            <input className="input_bar2" type="password" onChange={(e)=>this.setState({password_comfirm: e.target.value})}/>
                        </div>
                    </form>
                    <button className="login_btn_now" onClick={this.registerRequest}>注册</button>
                    <button className="login_btn" onClick={()=>this.setState({loginMode: true})}>登录</button>
                </div>
            )
        }
        if(this.state.redirect)
            return <Redirect push to="/data-manip"/>;
        return (
            <div className="login_block">
                {content}
            </div>
        )
    }
}

class App extends React.Component{
    render(){
        return (
            <div className="App">
                <header className="App-header">
                    <strong className="title-name">TD-LTE查询管理系统</strong>
                    <img src={logo} className="App-logo" alt="logo" />
                </header>
                <body className="body_style">
                    <LoginEnd />
                </body>
            </div>
        );
    }
}

export default App;
