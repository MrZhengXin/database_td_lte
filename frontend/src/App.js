import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import {Redirect} from 'react-router-dom';

const ipaddr = 'https://127.0.0.1/';

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
        alert("login");
        axios.post(ipaddr + 'account/login/', {
            "login": this.state.username,
            "password": this.state.password
        }).then((response)=>{
                console.log('response: ' + response)
        }).catch((e)=>{
            console.log('error: ' + e)
        });
        //登录成功后
        this.setState({redirect: true});
    }

    registerRequest(){
        alert("register");
        axios.post(ipaddr + 'account/login/', {
            "username": this.state.username,
            "first_name": this.state.first_name,
            "last_name": this.state.last_name,
            "email": this.state.email,
            "password": this.state.password,
            "password_confirm": this.state.password_comfirm
        }).then((response)=>{
            console.log('response: ' + response)
        }).catch((e)=>{
            console.log('error: ' + e)
        })
    }

    render(){
        let content;
        if (this.state.loginMode){
            content = (
                <div>
                    <form>
                        <div className="style_table">
                            <b className="font_style">用户名：</b>
                            <input type="text" onChange={(e)=>this.setState({username: e.target.value})}/>
                        </div>
                        <div className="style_table">
                            <b className="font_style">密 码：</b>
                            <input type="text" onChange={(e)=>this.setState({password: e.target.value})}/>
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
                            <input type="text" onChange={(e)=>this.setState({username: e.target.value})}/>
                        </div>
                        <div className="style_table">
                            <b className="font_style">姓 氏：</b>
                            <input type="text" onChange={(e)=>this.setState({first_name: e.target.value})}/>
                        </div>
                        <div className="style_table">
                            <b className="font_style">名 字：</b>
                            <input type="text" onChange={(e)=>this.setState({last_name: e.target.value})}/>
                        </div>
                        <div className="style_table">
                            <b className="font_style">邮 箱：</b>
                            <input type="text" onChange={(e)=>this.setState({email: e.target.value})}/>
                        </div>
                        <div className="style_table">
                            <b className="font_style">密 码：</b>
                            <input type="text" onChange={(e)=>this.setState({password: e.target.value})}/>
                        </div>
                        <div className="style_table">
                            <b className="font_style">密码确认：</b>
                            <input type="text" onChange={(e)=>this.setState({password_comfirm: e.target.value})}/>
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
