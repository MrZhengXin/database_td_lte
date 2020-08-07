
import ReactEcharts from 'echarts-for-react';
import React, { Component } from 'react';// 引入 ECharts 主模块

import echarts from 'echarts/lib/echarts';// 引入柱状图
import 'echarts/lib/chart/bar';// 引入提示框和标题组件
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/title';

class MyChart extends React.Component{
    constructor(props) {
        super(props);
    }

    render(){
        return(
            <div>
                <ReactEcharts
                    option={
                        {
                            title: {
                                text: 'KPI属性指标在日期上的变化'
                            },
                            // tooltip: {
                            //     trigger: 'axis'
                            // },
                            legend: {
                                data:['属性']
                            }, //线标
                            toolbox: {
                                show: true,
                                feature: {
                                    dataZoom: {
                                        yAxisIndex: 'none'
                                    },
                                    dataView: {readOnly: false},
                                    magicType: {type: ['line', 'bar']},
                                    restore: {},
                                    saveAsImage: {}
                                }
                            },
                            xAxis:  {
                                type: 'time',
                                // boundaryGap: false,
                                // data: ['2017-5-6', '2017-7-10', '2017-8-20'] // this.props.xItems
                            },
                            yAxis: {
                                type: 'value',
                                axisLabel: {
                                    formatter: '{value}'
                                }
                            },
                            series: [
                                {
                                    name:'属性值',
                                    type:'line',
                                    data: this.props.items,
                                    // markPoint: {
                                    //     data: [
                                    //         {type: 'max', name: '最大值'},
                                    //         {type: 'min', name: '最小值'}
                                    //     ]
                                    // },
                                    // markLine: {
                                    //     data: [
                                    //         {type: 'average', name: '平均值'}
                                    //     ]
                                    // }
                                },
                                // {
                                //     name:'最低气温',
                                //     type:'line',
                                //     data:[1, -2, 2, 5, 3, 2, 0],
                                    // markPoint: {
                                    //     data: [
                                    //         {name: '周最低', value: -2, xAxis: 1, yAxis: -1.5}
                                    //     ]
                                    // },
                                    // markLine: {
                                    //     data: [
                                    //         {type: 'average', name: '平均值'},
                                    //         [{
                                    //             symbol: 'none',
                                    //             x: '90%',
                                    //             yAxis: 'max'
                                    //         }, {
                                    //             symbol: 'circle',
                                    //             label: {
                                    //                 normal: {
                                    //                     position: 'start',
                                    //                     formatter: '最大值'
                                    //                 }
                                    //             },
                                    //             type: 'max',
                                    //             name: '最高点'
                                    //         }]
                                    //     ]
                                    // }
                                // }
                            ]
                        }
                    }
                     style={{height: '400px', width: '900px'}}
                />
            </div>
        )
    }
}

export default MyChart;