import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import './DataLoad.css';
import MyChart from '../source/MyChart'
import axios from 'axios';
import moment from 'moment';

const ipaddr = 'http://127.0.0.1:8000/';
const tbName = ['1.tbCell.xlsx', '2.tbAdjCell.xlsx', '3.tbSecAdjCell.xls', '4.tbOptCell.xlsx', '5.tbPCIAssignment.xlsx',
    '6.tbATUData.csv', '7.tbATUC2I.xlsx', '8.tbATUHandOver.csv', '9.tbMROData.csv', '10.tbC2I.xlsx', '11.tbHandOver.xlsx',
    '12.tbKPI.xlsx', '13.tbPRB.xlsx']
const download = ['tbATUC1I', 'tbPCIAssignment', 'tbATUHandOver', 'tbOptCell']

var formatDateTime = function (date) {
    var y = date.getFullYear();
    var m = date.getMonth() + 1;
    m = m < 10 ? ('0' + m) : m;
    var d = date.getDate();
    d = d < 10 ? ('0' + d) : d;
    var h = date.getHours();
    h = h < 10 ? ('0' + h) : h;
    var minute = date.getMinutes();
    minute = minute < 10 ? ('0' + minute) : minute;
    var second=date.getSeconds();
    second=second < 10 ? ('0' + second) : second;
    return m + '/' + d + '/' + y +' '+h+':'+minute+':'+second;
};

class InfoQuery extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            model: 'cell',
            selfInput: true,  // 手动输入 选择输入
            modelInput: 'name',  // 搜索模式

            cellID: '',
            cellName: '',
            cellIDs: [],
            cellNames: [],
            name_list: [],
            data_list: [],

            eNodeBID: '',
            eNodeBName: '',
            eNodeBMsgName: [],
            eNodeBMsgData: [],
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
        this.queryENodeB = this.queryENodeB.bind(this);
        this.queryKPI = this.queryKPI.bind(this);
    }

    querySelection(event){
        console.log('selfInput: ' + this.state.selfInput);
        if(this.state.selfInput){
            console.log('model: ' + this.state.model);
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
                    axios.get(ipaddr + 'query/tbKPI/?NE_list=True')
                        .then((response)=>{
                            console.log('data length: ' + response.data.length);
                            this.setState({neNames: response.data});
                        })
                        .catch((e) => {
                            console.log('err: ' + e);
                        });
                }
            }else if(this.state.model === 'prb'){
                if(this.state.pneNames.length <= 0){
                    axios.get(ipaddr + 'query/tbKPI/?NE_list=True')
                        .then((response)=>{
                            console.log('data: ' + response.data);
                            this.setState({pneNames: response.data});
                        })
                        .catch((e) => {
                            console.log('err: ' + e);
                        });
                }
            }
        }
        this.setState((state)=>({selfInput: !state.selfInput}));
        event.preventDefault();
    }

    queryCell(event){
        var queryStr = '';
        if(this.state.modelInput === 'id' && this.state.cellID.length > 0){
            queryStr = 'attribute=SECTOR_ID&value=' + this.state.cellID;
        }else if(this.state.modelInput === 'name' && this.state.cellName.length > 0){
            queryStr = 'attribute=SECTOR_NAME&value=' + this.state.cellName;
        }
        if(queryStr === ''){
            alert('no input');
        }else{
            axios.get(ipaddr + '/query/tbCell/?' + queryStr)
                .then((response)=> {
                    var attr_name_list = [], data_list = [];
                    if(response.data.length > 0){
                        for (var ky in response.data[0])
                            attr_name_list = [...attr_name_list, ky];
                        for(var i = 0; i < response.data.length; i++){
                            var temp_list = [];
                            for(var ky in response.data[i]){
                                temp_list = [...temp_list, response.data[i][ky]];
                            }
                            data_list = [...data_list, temp_list];
                        }
                        this.setState({name_list: attr_name_list, data_list: data_list});
                    }else{
                        this.setState({name_list: [], data_list: []});
                        alert('no data searched');
                    }
                })
                .catch((e)=>console.log('error: ' + e));
        }
        event.preventDefault();
    }

    queryENodeB(event){
        var queryStr = '';
        // console.log('input: ' + this.state.modelInput + this.state.eNodeBName + this.state.eNodeBID);
        if(this.state.modelInput === 'id' && this.state.eNodeBID.length > 0){
            queryStr = 'attribute=ENODEBID&value=' + this.state.eNodeBID;
        }else if(this.state.modelInput === 'name' && this.state.eNodeBName.length > 0){
            queryStr = 'attribute=ENODEB_NAME&value=' + this.state.eNodeBName;
        }
        if(queryStr === ''){
            alert('no input');
        }else{
            axios.get(ipaddr + '/query/tbCell/?' + queryStr)
                .then((response)=> {
                    var attr_name_list = [], data_list = [];
                    if(response.data.length > 0){
                        for (var ky in response.data[0])
                            attr_name_list = [...attr_name_list, ky];
                        for(var i = 0; i < response.data.length; i++){
                            var temp_list = [];
                            for(var ky in response.data[i]){
                                temp_list = [...temp_list, response.data[i][ky]];
                            }
                            data_list = [...data_list, temp_list];
                        }
                        this.setState({eNodeBMsgName: attr_name_list, eNodeBMsgData: data_list});
                    }else{
                        this.setState({name_list: [], data_list: []});
                        alert('no data searched');
                    }
                })
                .catch((e)=>console.log('error: ' + e));
        }
        event.preventDefault();
    }

    queryKPI(e){
        if(this.state.neName.length > 0 && this.state.attr.length > 0) {
            var qry = 'query/tbKPI/?NE=' + this.state.neName + '&attribute=' +
                this.state.attr + '&l=' + moment(this.state.beg).format("MM/DD/YYYY HH:mm:ss") + '&r=' +
                moment(this.state.end).format("MM/DD/YYYY HH:mm:ss");
            console.log('qry: ' + qry);
            axios.get(ipaddr + qry)
                .then((response)=>{
                    console.log('data: ' + response.data);
                    this.setState({date_vals: response.data});
                })
                .catch((e)=>console.log('error: ' + e));
        }else{
            alert('no input');
        }
        e.preventDefault();
    }

    queryPRB(e){
        if(this.state.pneName.length > 0 && this.state.pattr.length > 0) {
            var qry = ipaddr + 'query/tbPRB/?NE=' + this.state.pneName + '&attribute=' +
                this.state.pattr + '$attribute_list=False&l=' + moment(this.state.beg).format("MM/DD/YYY HH:mm:ss") + '&r=' +
                moment(this.state.end).format("MM/DD/YYY HH:mm:ss");
            console.log('qry' + qry);
            axios.get(qry)
                .then((response)=>{
                    console.log('data:' + response.data);
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
                        <select className="input_bar" onChange={(e)=>this.setState({modelInput: e.target.value})}>
                            <option value="name">按SECTOR_NAME搜索</option>
                            <option value="id">按SECTOR_ID搜索</option>
                        </select>
                        <button className="right_align" onClick={this.querySelection}>{this.state.selfInput ? '快速选择' : '输入搜索'}</button>
                    </div>
                    <form onSubmit={this.queryCell}>
                        {this.state.modelInput === "id" &&
                            <label className="vt_margin">
                                <span>小区ID: </span>
                                {this.state.selfInput ?
                                    <input className="input_bar" type="text" onChange={(e)=>this.setState({cellID: e.target.value})}/> :
                                    <select className="input_bar" value={this.state.cellID} onChange={(e)=>{this.setState({cellID: e.target.value});console.log('cellID: '+ this.state.cellID);}}>
                                        <option value="">------请选择------</option>
                                        {this.state.cellIDs.map((item)=><option value={item}>{item}</option>)}
                                    </select>}
                            </label>}
                        {this.state.modelInput === "name" &&
                            <label className="vt_margin">
                            <span>小区名: </span>
                            {this.state.selfInput ?
                                <input className="input_bar" type="text" onChange={(e)=>this.setState({cellName: e.target.value})}/> :
                                <select className="input_bar" onChange={(e)=>this.setState({cellName: e.target.value})}>
                                    <option value="">------请选择------</option>
                                    {this.state.cellNames.map((item)=><option value={item}>{item}</option>)}
                                </select>}
                            </label>
                        }
                        <button type="submit" className="menu_btn">确认</button>
                    </form>
                    {this.state.data_list.length > 0 &&
                    <table>
                        <tr key="title" className="text_strong">
                            {
                                this.state.name_list.map((key)=>(
                                <th align="center" valign="middle">{key}</th>
                            ))
                            }
                        </tr>
                        {this.state.data_list.map((item)=>(
                            <tr key={item.SECTOR_ID} className="text_color">
                                {
                                    item.map((key)=>(
                                    <th key={key} align="center" valign="middle">{key}</th>
                                ))
                                }
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
                        <span>请选择搜索模式</span>
                        <select className="input_bar" onChange={(e)=>this.setState({modelInput: e.target.value})}>
                            <option value="name">按ENODEB_NAME搜索</option>
                            <option value="id">按ENODEBID搜索</option>
                        </select>
                        <button className="right_align" onClick={this.querySelection}>{this.state.selfInput ? '快速选择' : '输入搜索'}</button>
                    </div>
                    <form onSubmit={this.queryENodeB}>
                        {this.state.modelInput === 'id' && <label className="vt_margin">
                            <span>基站ID: </span>
                            {this.state.selfInput ?
                                <input className="input_bar" type="text" onChange={(e)=>this.setState({eNodeBID: e.target.value})}/> :
                                <select className="input_bar" onChange={(e)=>this.setState({eNodeBID: e.target.value})}>
                                    <option value={""}>{"------请选择------"}</option>
                                    {this.state.eNodeBIDs.map((item)=><option value={item}>{item}</option>)}
                                </select>}
                        </label>}
                        {this.state.modelInput === 'name' && <label className="vt_margin">
                            <span>基站名: </span>
                            {this.state.selfInput ?
                                <input className="input_bar" type="text" onChange={(e)=>this.setState({eNodeBName: e.target.value})}/> :
                                <select className="input_bar" onChange={(e)=>this.setState({eNodeBName: e.target.value})}>
                                    <option value={""}>{"------请选择------"}</option>
                                    {this.state.eNodeBNames.map((item)=><option value={item}>{item}</option>)}
                                </select>}
                        </label>}
                        <button type="submit" className="menu_btn">确认</button>
                    </form>
                    {this.state.eNodeBMsgData.length > 0 &&
                    <table>
                        <tr className="text_strong">
                            {this.state.eNodeBMsgName.map((key)=>(
                                <th align="center" valign="middle">{key}</th>
                            ))}
                        </tr>
                        {this.state.eNodeBMsgData.map((item)=>(
                            <tr className="text_color">
                                {item.map((key)=>(
                                    <th align="center" valign="middle">{key}</th>
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
                        <span className="left_align">请输入要查询的kpi信息</span>
                        <button className="in_visiable"/>
                        <button className="right_align" onClick={this.querySelection}>{this.state.selfInput ? '快速选择' : '输入搜索'}</button>
                    </div>
                    <form onSubmit={this.queryKPI}>
                        <label className="vt_margin">
                            <span>网元名称: </span>
                            {this.state.selfInput ?
                                <input className="input_bar" type="text" onChange={(e)=>this.setState({neName: e.target.value})}/> :
                                <select className="input_bar" onChange={(e)=>this.setState({neName: e.target.value})}>
                                    <option value="">------请选择------</option>
                                    {this.state.neNames.map((item)=><option value={item}>{item}</option>)}
                                </select>}
                        </label>
                        <label className="vt_margin">
                            <span>属性名称: </span>
                            <select className="input_bar"  onChange={(e)=>this.setState({attr: e.target.value})}>
                                <option value="">------请选择------</option>
                                {this.state.attrs.map((item)=><option value={item}>{item}</option>)}
                            </select>
                        </label>
                        <label className="vt_margin">
                            <span>起始时间：</span>
                            <input type="datetime-local" onChange={(e)=>this.setState({beg: e.target.value})}/>
                        </label><br/>
                        <label className="vt_margin">
                            <span>结束时间：</span>
                            <input type="datetime-local" onChange={(e)=>this.setState({end: e.target.value})}/>
                        </label>
                        <button type="submit" className="menu_btn">确认</button>
                    </form>
                    {this.state.date_vals.length > 0 &&
                    <MyChart items={this.state.date_vals} table={'KPI'} attr={this.state.attr}/>
                    }
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
                        <span className="left_align">请输入要查询的PRB相关信息：</span>
                        <button className="in_visiable"/>
                        <button className="right_align" onClick={this.querySelection}>{this.state.selfInput ? '快速选择' : '输入搜索'}</button>
                    </div>
                    <div>
                    <form onSubmit={this.queryPRB}>
                        <label className="vt_margin">
                            <span>网元名称: </span>
                            {this.state.selfInput ?
                                <input className="input_bar" type="text" onChange={(e)=>this.setState({pneName: e.target.value})}/> :
                                <select className="input_bar" onChange={(e)=>this.setState({pneName: e.target.value})}>
                                    <option value={""}>------请输入------</option>
                                    {this.state.pneNames.map((item)=><option value={item}>{item}</option>)}
                                </select>}
                        </label>
                        <label className="vt_margin">
                            <span>属性名称: </span>
                            <select className="input_bar" onChange={(e)=>this.setState({pattr: e.target.value})}>
                                <option value={""}>------请输入------</option>
                                {this.state.pattrs.map((item)=><option value={item}>{item}</option>)}
                            </select>
                        </label>
                        <label className="vt_margin">
                            <span>起始时间：</span>
                            <input type="datetime-local" onChange={(e)=>this.setState({beg: e.target.value})}/>
                        </label><br/>
                        <label className="vt_margin">
                            <span>结束时间：</span>
                            <input type="datetime-local" onChange={(e)=>this.setState({end: e.target.value})}/>
                        </label>
                        <button type="submit" className="menu_btn">确认</button>
                    </form>
                    </div>
                    {
                        this.state.pdate_vals.length > 0 &&
                        <MyChart items={this.state.pdate_vals} table={'PRB'} attr={this.state.pattr}/>
                    }
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