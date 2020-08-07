import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import './DataLoad.css';
import axios from 'axios';

const ipaddr = '127.0.0.1/'
const tbName = ['1.tbCell.xlsx', '2.tbAdjCell.xlsx', '3.tbSecAdjCell.xls', '4.tbOptCell.xlsx', '5.tbPCIAssignment.xlsx',
    '6.tbATUData.csv', '7.tbATUC2I.xlsx', '8.tbATUHandOver.csv', '9.tbMROData.csv', '10.tbC2I.xlsx', '11.tbHandOver.xlsx',
    '12.tbKPI.xlsx', '13.tbPRB.xlsx']
const download = ['tbATUC1I', 'tbPCIAssignment', 'tbATUHandOver', 'tbOptCell']

class MultCover extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            rate: ''
        }
        this.reqTbC2I3 = this.reqTbC2I3.bind(this);
    }

    reqTbC2I3(e){
        if(/^0.\d+$/.test(this.state.rate)){
            var rt = parseFloat(this.state.rate);
            console.log('rate: ' + rt.toString());
            if(rt > 0.0 && rt < 1.0){
                axios.get(ipaddr + 'create/tbC2I3/?rate=' + this.state.rate)
                    .then((rsp)=> {
                        rsp.blob().then(blob => {
                            let blobUrl = window.URL.createObjectURL(blob);
                            let a = document.createElement('a_id');
                            let filename = rsp.headers.get('Content-Disposition');
                            a.href = blobUrl;
                            a.download = filename;
                            a.click();
                            window.URL.revokeObjectURL(blobUrl);
                        });
                    })
                    .catch((e) => console.log('err: ' + e));
            }else{
                alert('input number must > 0.0 and < 1.0');
            }
        }else if(this.state.rate === ''){
            alert('no input');
        }else{
            alert('input must be a number and input number must > 0.0 and < 1.0');
        }
    }

    render(){
        let content;
        content = (
            <div>
                <div>
                    <p className="line_style"/>
                    <div className="sub_title">查询重叠覆盖干扰三元组</div>
                    <p className="line_style"/>
                </div>
                <div>
                    <form onSubmit={this.reqTbC2I3}>
                        <span>PrbABS6最小概率数（0.0-1.0）：</span>
                        <input typeof="text" onChange={(e)=>this.setState({rate: e.target.value})}/>
                        <button type="submit">数据导出</button>
                    </form>
                </div>
            </div>
        )
        return (
            <div className="App">
                <div className="App-header">
                    <h2 className="title-name">TD-LTE查询管理系统</h2>
                </div>
                <body>
                    <div className="bg bg-blur"></div>
                    <div className="menu">
                        <button className="menu_btn" onClick={()=>{this.props.history.push('/data-manip/data-load')}}>数据管理</button>
                        <button className="menu_btn" onClick={()=>{this.props.history.push('/data-manip/info-query')}}>信息查询</button>
                        <button className="menu_btn" onClick={()=>{this.props.history.push('/data-manip/C2I-analyse')}}>主邻小区C2I干扰分析</button>
                        <button className="menu_btn_now" onClick={()=>{this.props.history.push('/data-manip/mult-cover')}}>查询重叠覆盖干扰三元组</button>
                    </div>
                    <div className="content">
                        {content}
                    </div>
                </body>
            </div>
        )
    }
}

export default MultCover;