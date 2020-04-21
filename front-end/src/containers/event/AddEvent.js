import React, { Component } from "react";
import { addEvent } from "./action";
import { connect } from "react-redux";
import { history } from "../../Routes";
class AddEvent extends Component {
  state = {
    data: {
      Name: "",
      Date_of_event: "",
      Venue: "",
      Operator_id: this.props.Operator_id,
    },
  };

  handleChange = (e) => {
    const key = e.target.name;
    let { data } = this.state;
    data[key] = e.target.value;
    this.setState({ data });
  };
  add = (e) => {
    e.preventDefault();
    const { data } = this.state;
    const { Name, Date_of_event, Venue, Operator_id } = data;
    if (Name && Date_of_event && Venue && Operator_id) {
      this.props.addEvent(data, () => {
        history.push("/");
      });
    } else {
      alert("Please enter valid data");
    }
  };
  render() {
      
    const { Name, Date_of_event, Venue } = this.state.data;
    debugger;
    return (
      <div className="card" style={{ textAlign: "left", padding: "10px" }}>
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>Add Event</h4>
        <form onSubmit={this.add}>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Event Name : </label>
            <input
              type="text"
              name="Name"
              value={Name}
              onChange={this.handleChange}
            />
          </div>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Date : </label>
            <input
              type="date"
              name="Date_of_event"
              value={Date_of_event}
              onChange={this.handleChange}
            />
          </div>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <label>Venue : </label>
            <input
              type="text"
              name="Venue"
              value={Venue}
              onChange={this.handleChange}
            />
          </div>
          <div style={{ margin: "10px", display: "inline-block" }}>
            <button type="submit" className="commonbtn">
              Add
            </button>
          </div>
        </form>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    Operator_id: state.auth.loginData.Operator_id,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    addEvent: (data, callback) => {
      dispatch(addEvent(data, callback));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(AddEvent);
