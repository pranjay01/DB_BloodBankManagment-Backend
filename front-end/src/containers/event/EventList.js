import React, { Component } from "react";
import { getAllEvents, deleteEvent } from "./action";
import { connect } from "react-redux";
import { history } from "../../Routes";
class EventList extends Component {
  componentDidMount() {
    this.props.getData();
  }
  deleteEvent = (Drive_id) => {
    this.props.deleteEvent(Drive_id, () => {
      this.props.getData();
    });
  };
  render() {
    let { data } = this.props;
    // data = [
    //   {
    //     Drive_id: 1,
    //     Name: "Red Cross drive",
    //     Date_of_event: "01/22/2020",
    //     Venue: "SJSU",
    //   },
    //   {
    //     Drive_id: 2,
    //     Name: "Prathma drive",
    //     Date_of_event: "01/22/2020",
    //     Venue: "Santa clara",
    //   },
    //   {
    //     Drive_id: 3,
    //     Name: "Salman drive",
    //     Date_of_event: "01/22/2020",
    //     Venue: "Villa",
    //   },
    // ];
    return (
      <div className="card">
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
          List of Events
          <button
            className="commonbtn"
            style={{ float: "right", marginRight: "10px" }}
            onClick={() => {
              history.push("/AddEvent");
            }}
          >
            Add Event
          </button>
        </h4>
        <div
          style={{
            textAlign: "left",
            marginLeft: "10px",
            marginRight: "10px",
            borderBottom: "grey solid 1px",
            marginBottom: "5px",
            cursor: "pointer",
          }}
        >
          <div style={{ minWidth: "300px", display: "inline-block" }}>
            Event Name
          </div>
          <div style={{ minWidth: "200px", display: "inline-block" }}>
            Event Date
          </div>
          <div style={{ minWidth: "300px", display: "inline-block" }}>
            Event Venue
          </div>
          <div style={{ minWidth: "50px", display: "inline-block" }}>Edit</div>
          <div style={{ minWidth: "50px", display: "inline-block" }}>
            Delete
          </div>
        </div>
        {data.map((item) => (
          <EventRow data={item} delete={this.deleteEvent} />
        ))}
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    data: state.app.allEvents,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getData: () => {
      dispatch(getAllEvents());
    },
    deleteEvent: (Drive_id, callback) => {
      dispatch(deleteEvent(Drive_id, callback));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(EventList);

class EventRow extends Component {
  delete = () => {
    const { data } = this.props;
    this.props.delete(data.Drive_id);
  };
  render() {
    const { data: item } = this.props;
    return (
      <div
        style={{
          textAlign: "left",
          marginLeft: "10px",
          marginRight: "10px",
          borderBottom: "grey solid 1px",
          marginBottom: "5px",
          cursor: "pointer",
        }}
      >
        <div style={{ minWidth: "300px", display: "inline-block" }}>
          {item.Name}
        </div>
        <div style={{ minWidth: "200px", display: "inline-block" }}>
         {item.Date_of_event.split(" 00:00:00 GMT")[0]}
        </div>
        <div style={{ minWidth: "300px", display: "inline-block" }}>
          {item.Venue}
        </div>
        <div
          style={{ minWidth: "50px", display: "inline-block" }}
          onClick={() => {
            history.push(`/UpdateEvent/${item.Drive_id}`);
          }}
        >
          <a href="#">Edit</a>
        </div>
        <div
          style={{ minWidth: "50px", display: "inline-block" }}
          onClick={this.delete}
        >
          <a href="#">Delete</a>
        </div>
      </div>
    );
  }
}
