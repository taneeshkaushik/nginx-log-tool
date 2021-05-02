import {combineReducers} from 'redux';
import userReducer from './user.reducers';
import instanceReducer from './instance.reducers';
import timeseriesReducer from './timeseries.reducers';
import timestampReducer from './timestamp.reducer';
import notificationReducer from './notification.reducer';
import agentReducer from './agent.reducer';

const appReducer =  combineReducers({
    userData: userReducer,
    instanceData: instanceReducer,
    timeseriesData: timeseriesReducer,
    timestamp:timestampReducer,
    notificationData:notificationReducer,
    myagent: agentReducer,
})

export default appReducer;