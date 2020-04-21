import React, { Component } from "react";
import { connect } from "react-redux";
import { addBloodCountForBloodBank } from "../../reducer/appReducer";
import { getBloodCountForBloodBank } from "./action";
import { history } from "../../Routes";
class BlooCountForBloodBank extends Component {
  componentDidMount() {
    this.props.getData(1);
  }
  componentWillUnmount() {
    this.props.reset();
  }
  render() {
    let { data } = this.props;
    // data = [
    //   {
    //     Br_id:1,
    //     Br_Type: "Main",
    //     Blood_Unit_Count: 30,
    //   },
    //   {
    //     Br_id:2,
    //     Br_Type: "Sub",
    //     Blood_Unit_Count: 10,
    //   },
    // ];
    return (
      <div>
        <h4 style={{ textAlign: "left", paddingLeft: "10px" }}>
          Branch wise blood unit availability
        </h4>
        {data &&
          data.map((item) => {
            return <BlooCountForBloodBankItem data={item} />;
          })}
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    data: state.app.bloodCountForBloodBank,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    getData: (Bbank_id) => {
      dispatch(getBloodCountForBloodBank(Bbank_id));
    },
    reset: () => {
      dispatch(addBloodCountForBloodBank([]));
    },
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(BlooCountForBloodBank);

class BlooCountForBloodBankItem extends Component {
  redirect = () => {
    const { data } = this.props;
    history.push(`/branch/bloodunits/${data.Br_id}/${data.Br_Type}`);
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
        onClick={this.redirect}
      >
        <a href="#">{item.Br_Type}</a>
        <span style={{ float: "right" }}>
          <b>{item.Blood_Unit_Count}</b> Units
        </span>
      </div>
    );
  }
}
