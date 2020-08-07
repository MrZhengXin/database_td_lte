import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import './DataLoad.css';
import MyChart from '../source/MyChart'
import axios from 'axios';

const ipaddr = '127.0.0.1/'
const tbName = ['1.tbCell.xlsx', '2.tbAdjCell.xlsx', '3.tbSecAdjCell.xls', '4.tbOptCell.xlsx', '5.tbPCIAssignment.xlsx',
    '6.tbATUData.csv', '7.tbATUC2I.xlsx', '8.tbATUHandOver.csv', '9.tbMROData.csv', '10.tbC2I.xlsx', '11.tbHandOver.xlsx',
    '12.tbKPI.xlsx', '13.tbPRB.xlsx']
const download = ['tbATUC1I', 'tbPCIAssignment', 'tbATUHandOver', 'tbOptCell']

function ListItem(props){
    return (
        <tr className="text_color">
            <th align="center" valign="middle">{}</th>
        </tr>
    );
}

class InfoQuery extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            model: 'cell',
            selfInput: true,

            cellID: '',
            cellName: '',
            cellIDs: [],
            cellNames: [],
            message: [],

            eNodeBID: '',
            eNodeBName: '',
            eNodeBMsg: [],
            eNodeBIDs: [],
            eNodeBNames: [],

            neName: '',
            neNames: [],
            attr: '',
            attrs: [],
            beg: new Date(),
            end: new Date(),
            date_vals: [],

            pneName: '',
            pneNames: [],
            pattr: '',
            pattrs: [],
            pdate_vals: []
        }
        this.queryCell = this.queryCell.bind(this);
        this.querySelection = this.querySelection.bind(this);
        this.queryPRB = this.queryPRB.bind(this);
    }

    querySelection(event){
        if(this.state.selfInput){
            if(this.state.model === 'cell'){
                if(this.state.cellIDs.length <= 0) {
                    axios.get(ipaddr + 'query/tbCell/?attribute=SECTOR_ID&value=-1')
                        .then((response) => {
                            console.log('data length: ' + response.data.length);
                            this.setState({cellIDs: response.data});
                        })
                        .catch((e) => {
                            console.log('err: ' + e)
                        });
                }
                if (this.state.cellNames.length <= 0){
                    axios.get(ipaddr + 'query/tbCell/?attribute=SECTOR_NAME&value=-1')
                        .then((response) => {
                            console.log('data length: ' + response.data.length);
                            this.setState({cellNames: response.data});
                        })
                        .catch((e) => {
                            console.log('err: ' + e);
                        });
                }
            }else if(this.state.model === 'enodeb'){
                if(this.state.eNodeBIDs.length <= 0) {
                    axios.get(ipaddr + 'query/tbCell/?attribute=ENODEBID&value=-1')
                        .then((response) => {
                            console.log('data length: ' + response.data.length);
                            this.setState({eNodeBIDs: response.data});
                        })
                        .catch((e) => {
                            console.log('err: ' + e)
                        });
                }
                if (this.state.eNodeBNames.length <= 0){
                    axios.get(ipaddr + 'query/tbCell/?attribute=ENODEB_NAME&value=-1')
                        .then((response) => {
                            console.log('data length: ' + response.data.length);
                            this.setState({eNodeBNames: response.data});
                        })
                        .catch((e) => {
                            console.log('err: ' + e);
                        });
                }
            }else if(this.state.model === 'kpi'){
                if(this.state.neNames.length <= 0){
                    // axios.get(ipaddr + 'query/tbKPI/?attribute_list=true')
                    //     .then((response)=>{
                    //         console.log('data length: ' + response.data.length);
                    //         this.setState({neNames: response.data});
                    //     })
                    //     .catch((e) => {
                    //         console.log('err: ' + e);
                    //     });
                }
            }else if(this.state.model === 'prb'){
                if(this.state.pneNames.length <= 0){
                    // 获取网元名称
                }
            }
        }
        event.preventDefault();
    }

    queryCell(event){
        if(this.state.cellID.length > 0 || this.state.cellName.length > 0){
            axios.get(ipaddr + '/query/tbCell/?attribute=' + this.state.cellID + '&value=' + this.state.cellName)
                .then((response)=> {
                    console.log('data legth: ' + response.data.length);
                    this.setState({message: response.data});
                })
                .catch((e)=>console.log('error: ' + e));
        }else{
            alert('no input');
        }
        event.preventDefault();
    }

    queryENodeB(event){
        if(this.state.eNodeBID.length > 0 || this.state.eNodeBName.length > 0){
            axios.get(ipaddr + 'query/tbCell/?attribute=' + this.state.eNodeBID + '&value=' + this.state.eNodeBName)
                .then((response)=>{
                    console.log('data length:' + response.data.length);
                    this.setState({eNodeBMsg: response.data});
                })
                .catch((e)=>console.log('error: ' + e));
        }else{
            alert('no input');
        }
        event.preventDefault();
    }

    queryKPI(e){
        if(this.state.eName.length > 0 && this.state.attr.length > 0) {
            axios.get(ipaddr + 'query/tbKPI/?NE=' + this.state.neName + '&attribute=' +
                this.state.attr + '&attribute_list=False&l=' + this.state.beg.format("MM/DD/YYY HH:mm:ss") + '&r=' +
                this.state.end.format("MM/DD/YYY HH:mm:ss"))
                .then((response)=>{
                    console.log('data length:' + response.data.length);
                    this.setState({date_vals: response.data})
                })
                .catch((e)=>console.log('error: ' + e));
        }else{
            alert('no input');
        }
        e.preventDefault();
    }

    queryPRB(e){
        if(this.state.pneName.length > 0 && this.state.pattr.length > 0) {
            axios.get(ipaddr + 'query/tbPRB/?NE=' + this.state.pneName + '&attribute=' +
                this.state.pattr + '&attribute_list=False&l=' + this.state.beg.format("MM/DD/YYY HH:mm:ss") + '&r=' +
                this.state.end.format("MM/DD/YYY HH:mm:ss"))
                .then((response)=>{
                    console.log('data length:' + response.data.length);
                    this.setState({pdate_vals: response.data})
                })
                .catch((e)=>console.log('error: ' + e));
        }else{
            alert('no input');
        }
        e.preventDefault();
    }


    render(){
        let content;
        if(this.state.model === 'cell'){
            content = (
                <div>
                    <div>
                        <p className="line_style"/>
                        <div className="sub_title">小区配置信息查询</div>
                        <p className="line_style"/>
                    </div>
                    <div>
                        <span>请输入小区ID或者小区名称</span>
                        <button onClick={()=>this.setState((state)=>({selfInput: !state.selfInput}))}>{this.state.selfInput ? '快速选择' : '输入搜索'}</button>
                    </div>
                    <form onSubmit={this.queryCell}>
                        <label>
                            <span>小区ID: </span>
                            {this.state.selfInput ?
                                <input type="text" onChange={(e)=>this.setState({cellID: e.target.value})}/> :
                                <select onChange={(e)=>this.setState({cellID: e.target.value})}>
                                    {this.state.cellIDs.map((item)=><option value={item}>{item}</option>)}
                                </select>}
                        </label><br/>
                        <label>
                            <span>小区名: </span>
                            {this.state.selfInput ?
                                <input type="text" onChange={(e)=>this.setState({cellName: e.target.value})}/> :
                                <select onChange={(e)=>this.setState({cellName: e.target.value})}>
                                    {this.state.cellNames.map((item)=><option value={item}>{item}</option>)}
                                </select>}
                        </label><br/>
                        <button type="submit" className="menu_btn">确认</button>
                    </form>
                    {this.state.message.length > 0 &&
                    <table>
                        <tr className="text_strong">
                            {this.state.message[0].map((key, val)=>(
                                <th align="center" valign="middle">key</th>
                            ))}
                        </tr>
                        {this.state.message.map((item)=>(
                            <tr className="text_color">
                                {item.map((key, val)=>(
                                    <th align="center" valign="middle">{val}</th>
                                ))}
                            </tr>
                        ))}
                    </table>}
                </div>
            );
        }else if(this.state.model === 'enodeb'){
            content = (
                <div>
                    <div>
                        <p className="line_style"/>
                        <div className="sub_title">基站eNodeB信息查询</div>
                        <p className="line_style"/>
                    </div>
                    <div>
                        <span>请输入基站ID或者基站名称</span>
                        <button onClick={()=>this.setState((state)=>({selfInput: !state.selfInput}))}>{this.state.selfInput ? '快速选择' : '输入搜索'}</button>
                    </div>
                    <form onSubmit={this.queryCell}>
                        <label>
                            <span>基站ID: </span>
                            {this.state.selfInput ?
                                <input type="text" onChange={(e)=>this.setState({eNodeBID: e.target.value})}/> :
                                <select onChange={(e)=>this.setState({eNodeBID: e.target.value})}>
                                    {this.state.eNodeBIDs.map((item)=><option value={item}>{item}</option>)}
                                </select>}
                        </label><br/>
                        <label>
                            <span>基站名: </span>
                            {this.state.selfInput ?
                                <input type="text" onChange={(e)=>this.setState({eNodeBName: e.target.value})}/> :
                                <select onChange={(e)=>this.setState({eNodeBName: e.target.value})}>
                                    {this.state.eNodeBNames.map((item)=><option value={item}>{item}</option>)}
                                </select>}
                        </label><br/>
                        <button type="submit" className="menu_btn">确认</button>
                    </form>
                    {this.state.eNodeBMsg.length > 0 &&
                    <table>
                        <tr className="text_strong">
                            {this.state.eNodeBMsg[0].map((key, val)=>(
                                <th align="center" valign="middle">key</th>
                            ))}
                        </tr>
                        {this.state.eNodeBMsg.map((item)=>(
                            <tr className="text_color">
                                {item.map((key, val)=>(
                                    <th align="center" valign="middle">{val}</th>
                                ))}
                            </tr>
                        ))}
                    </table>}
                </div>
            )
        }else if(this.state.model === 'kpi'){
            content =(
                <div>
                    <div>
                        <p className="line_style"/>
                        <div className="sub_title">KPI指标信息查询</div>
                        <p className="line_style"/>
                    </div>
                    <div>
                        <span>请输入网元名称</span>
                        <button onClick={()=>this.setState((state)=>({selfInput: !state.selfInput}))}>{this.state.selfInput ? '快速选择' : '输入搜索'}</button>
                    </div>
                    <form onSubmit={this.queryKPI}>
                        <label>
                            <span>网元名称: </span>
                            {this.state.selfInput ?
                                <input type="text" onChange={(e)=>this.setState({neName: e.target.value})}/> :
                                <select onChange={(e)=>this.setState({neName: e.target.value})}>
                                    {this.state.neNames.map((item)=><option value={item}>{item}</option>)}
                                </select>}
                        </label><br/>
                        <label>
                            <span>属性名称: </span>
                            <select onChange={(e)=>this.setState({attr: e.target.value})}>
                                {this.state.attrs.map((item)=><option value={item}>{item}</option>)}
                            </select>
                        </label><br/>
                        <label>
                            <span>起始时间：</span>
                            <input type="datetime-local" onChange={(e)=>this.setState({beg: e.target.value})}/>
                            <span>结束时间：</span>
                            <input type="datetime-local" onChange={(e)=>this.setState({end: e.target.value})}/>
                        </label>
                        <button type="submit" className="menu_btn">确认</button>
                    </form>
                    <MyChart xItems={this.state.date_vals} yItems={this.state.attr_vals}/>
                </div>
            )
        }else if(this.state.model === 'prb'){
            content =(
                <div>
                    <div>
                        <p className="line_style"/>
                        <div className="sub_title">PRB信息统计与查询</div>
                        <p className="line_style"/>
                    </div>
                    <div>
                        <span>请输入网元名称</span>
                        <button onClick={()=>this.setState((state)=>({selfInput: !state.selfInput}))}>{this.state.selfInput ? '快速选择' : '输入搜索'}</button>
                    </div>
                    <form onSubmit={this.queryPRB}>
                        <label>
                            <span>网元名称: </span>
                            {this.state.selfInput ?
                                <input type="text" onChange={(e)=>this.setState({pneName: e.target.value})}/> :
                                <select onChange={(e)=>this.setState({pneName: e.target.value})}>
                                    {this.state.pneNames.map((item)=><option value={item}>{item}</option>)}
                                </select>}
                        </label><br/>
                        <label>
                            <span>属性名称: </span>
                            <select onChange={(e)=>this.setState({pattr: e.target.value})}>
                                {this.state.pattrs.map((item)=><option value={item}>{item}</option>)}
                            </select>
                        </label><br/>
                        <label>
                            <span>起始时间：</span>
                            <input type="datetime-local" onChange={(e)=>this.setState({beg: e.target.value})}/>
                            <span>结束时间：</span>
                            <input type="datetime-local" onChange={(e)=>this.setState({end: e.target.value})}/>
                        </label>
                        <button type="submit" className="menu_btn">确认</button>
                    </form>
                    <MyChart items={this.state.pdate_vals}/>
                </div>
            )
        }
        return (
            <div className="App">
                <div className="App-header">
                    <h2 className="title-name">TD-LTE查询管理系统</h2>
                </div>
                <body>
                    <div className="bg bg-blur"></div>
                    <div className="menu">
                        <button className="menu_btn" onClick={()=>{this.props.history.push('/data-manip/data-load')}}>数据管理</button>
                        <button className="menu_btn_now" onClick={()=>{this.props.history.push('/data-manip/info-query')}}>信息查询</button>
                        <button className={this.state.model === 'cell' ? "sub_menu_now" : "sub_menu"} onClick={()=>{
                            this.setState({model: 'cell', selfInput: true});
                        }}>小区配置信息查询</button>
                        <button className={this.state.model === 'enodeb' ? "sub_menu_now" : "sub_menu"} onClick={()=>{
                            this.setState({model: 'enodeb', selfInput: true});
                        }}>基站eNodeB信息查询</button>
                        <button className={this.state.model === 'kpi' ? "sub_menu_now" : "sub_menu"} onClick={()=>{
                            this.setState({model: 'kpi', selfInput: true});
                            if(this.state.attrs.length <= 0){
                                axios.get(ipaddr + 'query/tbKPI/?attribute_list=true')
                                    .then((response)=>{
                                        console.log('data length: ' + response.data.length);
                                        this.setState({attrs: response.data});
                                    })
                                    .catch((e) => {
                                        console.log('err: ' + e);
                                    });
                            }
                        }}>KPI指标信息查询</button>
                        <button className={this.state.model === 'prb' ? "sub_menu_now" : "sub_menu"} onClick={()=>{
                            this.setState({model: 'prb', selfInput: true});
                            if(this.state.pattrs.length <= 0){
                                axios.get(ipaddr + 'query/tbPRB/?attribute_list=true')
                                    .then((response)=>{
                                        console.log('data length: ' + response.data.length);
                                        this.setState({pattrs: response.data});
                                    })
                                    .catch((e) => {
                                        console.log('err: ' + e);
                                    });
                            }
                        }}>PRB信息统计与查询</button>
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

export default InfoQuery;