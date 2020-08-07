import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import './DataLoad.css';
import axios from 'axios';

const ipaddr = '127.0.0.1/'
const tbName = ['1.tbCell.xlsx', '2.tbAdjCell.xlsx', '3.tbSecAdjCell.xls', '4.tbOptCell.xlsx', '5.tbPCIAssignment.xlsx',
    '6.tbATUData.csv', '7.tbATUC2I.xlsx', '8.tbATUHandOver.csv', '9.tbMROData.csv', '10.tbC2I.xlsx', '11.tbHandOver.xlsx',
    '12.tbKPI.xlsx', '13.tbPRB.xlsx']
const download = ['tbATUC1I', 'tbPCIAssignment', 'tbATUHandOver', 'tbOptCell']

class DataLoad extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            modelInput: true,
            inputFileName: '',
            outFileName: ''
        };
        this.fileInput = React.createRef();
        this.handleInputSubmit = this.handleInputSubmit.bind(this);
        this.handleOutputSubmit = this.handleOutputSubmit.bind(this);
    }

    componentDidMount(){
       if(this.fileInput)
           this.fileInput.focus();
    }

    handleInputSubmit(e){
        const data = new FormData();
        if(this.state.inputFileName.length > 0){  // this.state.inputFileName.length > 0
            console.log('file: ' + this.state.inputFileName);
            if (this.fileInput.current == null){
                console.log('current file is null');
            }else{
                data.append('file', this.fileInput.current.files[0]);  // document.getElementById('name').
                fetch(ipaddr + 'data-manip/data-load/upload', {
                    method: 'POST',
                    body: data
                }).then(response=>console.log('response: ' + response));
            }
        }else{
            console.log('no file chosed');
        }
        e.preventDefault();
    }

    handleOutputSubmit(e){
        if(this.state.outFileName.length > 0){
            fetch(ipaddr + this.state.outFileName, { //downloadFiles 接口请求地址
                method: 'get'
            }).then((response) => {
                response.blob().then(blob => {
                    let blobUrl = window.URL.createObjectURL(blob);
                    let aElement = document.getElementById('downloadDiv'); //获取a标签元素
                    let filename = 'filename' + '.zip';//设置文件名称
                    aElement.href = blobUrl;//设置a标签路径
                    aElement.download = filename;
                    aElement.click();
                    window.URL.revokeObjectURL(blobUrl);
                });
            }).catch((error) => {
                console.log('文件下载失败', error);
            });
        }
        e.preventDefault();
    }

    render(){
        let content;
        if(this.state.modelInput){
            content = (
                <div>
                    <div>
                        <p className="line_style"/>
                        <div className="sub_title">数据导入</div>
                        <p className="line_style"/>
                    </div>
                    <div>
                        <form onSubmit={this.handleInputSubmit}>
                            <div>
                                <span>导入文件: </span>
                                <input type="text" value={this.state.inputFileName} readOnly/>
                                <button
                                    type="button"  // 防止被默认为submit
                                    onClick={()=>{
                                        this.fileInput.click();
                                        console.log('button->input clicked');
                                    }}>浏览</button><br/>
                                <input type="submit" className="menu_btn" value="确定"/><br/>
                                <input
                                    type="file"
                                    accept=".xlsx, .xls, .csv"
                                    onChange={(e) => {
                                        console.log('inputFileName changed, path: ' + e.target.files[0].path);
                                        this.setState({inputFileName: e.target.value});
                                    }}
                                    id='import'
                                    ref={input => {this.fileInput = input; console.log(input);}}  // input => this.fileInput = input
                                    style={{opacity: 0}}/>
                            </div>
                        </form>
                    </div>
                </div>
            );
        }else{
            content = (
                <div>
                    <div>
                        <p className="line_style"/>
                        <div className="sub_title">数据导出</div>
                        <p className="line_style"/>
                    </div>
                    <div>
                        <form onSubmit={(e)=>this.handleOutputSubmit(e)}>
                            <div>
                                <span>选择要导出的数据表：</span>
                                <select onChange={(e)=>{this.setState({outFileName: e.target.value})}}>
                                    {download.map((name)=> <option value={name}>{name + "表"}</option>)}
                                </select>
                            </div>
                            <input type="submit" className="menu_btn" value="确定"/>
                        </form>
                    </div>
                </div>
            );
        }
        return(
            <div className="App">
                <div className="App-header">
                    <h2 className="title-name">TD-LTE查询管理系统</h2>
                </div>
                <body>
                    <div className="bg bg-blur"></div>
                    <div className="menu">
                        <button className="menu_btn_now" onClick={()=>{this.props.history.push('/data-manip/data-load')}}>数据管理</button>
                        <button className={this.state.modelInput ? "sub_menu_now" : "sub_menu"} onClick={()=>{
                            this.setState({modelInput: true});
                        }}>数据导入</button>
                        <button className={this.state.modelInput ? "sub_menu" : "sub_menu_now"} onClick={()=>{
                            this.setState({modelInput: false});
                        }}>数据导出</button>
                        <button className="menu_btn" onClick={()=>{this.props.history.push('/data-manip/info-query')}}>信息查询</button>
                        <button className="menu_btn" onClick={()=>{this.props.history.push('/data-manip/C2I-analyse')}}>主邻小区C2I干扰分析</button>
                        <button className="menu_btn" onClick={()=>{this.props.history.push('/data-manip/mult-cover')}}>查询重叠覆盖干扰三元组</button>
                    </div>
                    <div className="content">
                        {content}
                    </div>
                </body>
            </div>
        )
    }
}

export default DataLoad;