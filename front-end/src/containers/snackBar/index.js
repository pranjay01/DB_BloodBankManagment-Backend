import React, { Component } from "react";
import { connect } from "react-redux";
import Message from "./Message";
import "./index.scss";

class SnackBar extends Component {
  render() {
    const { snackbarData } = this.props;
    if (snackbarData.length === 0) return "";
    return (
      <div className="snackbar-container">
        {snackbarData.map((item, index) => (
          <Message data={item} key={`${index}_snackbar`} />
        ))}
      </div>
    );
  }
}

const mapStateToProps = state => ({
  snackbarData: state.app.snackbarData
});

export default connect(
  mapStateToProps,
  null
)(SnackBar);
