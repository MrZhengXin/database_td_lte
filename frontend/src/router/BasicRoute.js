import React from 'react';
import {HashRouter, Route, Switch} from 'react-router-dom';
import App from '../App';
import DataManip from '../DataManip';
import DataLoad from '../data-manip/DataLoad'
import InfoQuery from '../data-manip/InfoQuery'
import C2IAnalyse from '../data-manip/C2IAnalyse'
import MultCover from '../data-manip/MultCover'

const BasicRoute = ()=>(
    <HashRouter>
        <Switch>
            <Route exact path="/" component={App}/>
            <Route exact path="/data-manip" component={DataManip}/>
            <Route exact path="/data-manip/data-load" component={DataLoad}/>
            <Route exact path="/data-manip/info-query" component={InfoQuery}/>
            <Route exact path="/data-manip/C2I-analyse" component={C2IAnalyse}/>
            <Route exact path="/data-manip/mult-cover" component={MultCover}/>
        </Switch>
    </HashRouter>
)

export default BasicRoute;