import React from "react";
import { Spinner as BootstrapSpinner } from "react-bootstrap";
import { useSelector } from "react-redux";
import { getSLoading } from "store/common/selectors";

const SimpleLoading = () => {
  const loading = useSelector(getSLoading);
  // const loading = true;
  return (
    <>
      {loading && (
        <div className="d-flex justify-content-center align-items-center h-100 loading-spinner">
          <BootstrapSpinner animation="border" variant="primary" />
        </div>
      )}
    </>
  );
};

export default SimpleLoading;
