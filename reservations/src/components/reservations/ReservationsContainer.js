import React from 'react';
import DatePicker from "react-datepicker";
import {get} from '../axios/Axios.js';

import "react-datepicker/dist/react-datepicker.css";

export default class ReservationsContainer extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      startDate: null,
      excludedDates: []
    };
  }

  componentDidMount() {
    (async () => {
      try {
        let excludedDates = await get("http://127.0.0.1:8000/cozumel/test");
        let date = await excludedDates;
        console.log(date);
        let today = new Date(excludedDates);
        let yesterday = new Date('2020, 08, 13');
        this.setState({startDate: new Date(), excludedDates: [yesterday, today]});
      } catch(error) {
        console.log(error);
      }
    })();
  }

  handleChange = (startDate) => {
    this.setState({
      startDate
    });
  };

  render() {
    const { startDate } = this.state;

    return (
      <div className="datepickers">
        <label>Date:</label>
        <DatePicker 
        selected={startDate} 
        onChange={this.handleChange}
        excludeDates={this.state.excludedDates} />
      </div>
    );
  }
}