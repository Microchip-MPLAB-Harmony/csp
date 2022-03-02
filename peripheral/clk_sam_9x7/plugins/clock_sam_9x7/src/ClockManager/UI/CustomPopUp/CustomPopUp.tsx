import { Dialog } from "primereact/dialog";
import { Button } from "primereact/button";
import useForceUpdate from "use-force-update";
import PrimeReact from "primereact/api";
import {
  peripheralClockConfig_PopupHeadding,
  GenerickClock_PopupHeadding,
} from "../MainView/CustomButtons";
import PeripheralsConfiguration from "../PopUpContent/PeripheralsConfiguration";
import GenericClockConfiguration from "../PopUpContent/GenericClockConfiguration";

let dialogVisibleStatus = false;

let ActionId: {} | null | undefined;
export function PopupLoaderId(Id: string) {
  dialogVisibleStatus = true;
  ActionId = Id;
}

const GenericPopUp = () => {
  const update = useForceUpdate();

  PrimeReact.ripple = true;

  const onHide = () => {
    dialogVisibleStatus = false;
    update();
  };

  const renderFooter = () => {
    return (
      <div className="p-flex-row-reverse">
        <div>
          <Button
            type="button"
            className="p-button-raised p-button-rounded"
            label="Close"
            style={{ height: "2.5rem", fontSize: "14px" }}
            onClick={() => onHide()}
            autoFocus
          />
        </div>
      </div>
    );
  };

  return (
    <div className="dialog-demo">
      <div className="card">
        <Dialog
          visible={dialogVisibleStatus}
          maximizable={true}
          closeOnEscape
          closable
          focusOnShow
          modal
          header={ActionId}
          footer={renderFooter()}
          onHide={() => onHide()}
        >
          <div>
            {ActionId === peripheralClockConfig_PopupHeadding && (
              <PeripheralsConfiguration parentUpdate={update} />
            )}
            {ActionId === GenerickClock_PopupHeadding && (
              <GenericClockConfiguration parentUpdate={update} />
            )}
          </div>
        </Dialog>
      </div>
    </div>
  );
};

export default GenericPopUp;
