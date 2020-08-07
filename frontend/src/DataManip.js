import React from 'react';
import './DataManip.css';
import axios from 'axios';

const ipaddr = "127.0.0.1/"
const tbName = ['1.tbCell.xlsx', '2.tbAdjCell.xlsx', '3.tbSecAdjCell.xls', '4.tbOptCell.xlsx', '5.tbPCIAssignment.xlsx',
    '6.tbATUData.csv', '7.tbATUC2I.xlsx', '8.tbATUHandOver.csv', '9.tbMROData.csv', '10.tbC2I.xlsx', '11.tbHandOver.xlsx',
    '12.tbKPI.xlsx', '13.tbPRB.xlsx']

class DataManip extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            model: "dataManip",  // 数据操作模式：input, output, query, analyse
            dataFile: "1.tbCell.xlsx",
            doneFiles: []
        }
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(e){
        if (this.state.model === "input"){
            axios.post(ipaddr + 'data/import', {"file": this.state.dataFile})  // 导入数据请求
                .then((response)=>{
                    console.log("response: " + response);
                })
                .catch((error)=>console.log("error: " + error));
            this.setState((state)=>({doneFiles: [...state.doneFiles, state.dataFile]}));  // 将已经导入的数据归到一个表中
        }else if (this.state.model === "output"){
            var fileName = this.state.dataFile;
            if(fileName.indexOf('.') !== -1 && fileName.indexOf('.') < fileName.lastIndexOf('.')){
                var name = fileName.slice(fileName.indexOf('.') + 1, fileName.lastIndexOf('.'))
                axios.get(ipaddr + 'download/' + name)
                    .then((response)=> {
                        console.log("response: " + response);
                    })
                    .catch((error)=>console.log("error: " + error));
            }else {
                console.log("fileName format not right!")
            }
        }else if(this.state.model === "query"){
            const w = window.open('about:blank');
            w.location.herf('https://www.baidu.com');
        }
        e.preventDefault();
    }

    render(){
        let content = (
            <div>
                <span>数据操作模块</span>
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
                        <button className="menu_btn" onClick={()=>{this.props.history.push('/data-manip/nult-cover')}}>查询重叠覆盖干扰三元组</button>
                    </div>
                    <div className="content">
                        {content}
                    </div>
                </body>
            </div>
        )
    }
}

export default DataManip;