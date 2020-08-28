import React from 'react';
import ReservationsContainer from '../reservations/ReservationsContainer.js'
import "./App.css";

export class App extends React.Component {

    componentDidMount() {
        document.title = "Casa Del Buceo";
    }

    render() {
        return (
            <div className="main">
                <ReservationsContainer />
            </div>
        );
    }
}

export default App