import React from "react";
import ReactDOM from "react-dom";
import { GetButton } from "../../Common/UIComponent";
import GenericPopUp, { PopupLoaderId } from "../CustomPopUp/CustomPopUp";

export let peripheralClockConfig_PopupHeadding = "Peripheral Configuration";
export let GenerickClock_PopupHeadding = "Generic Clock Configuration";

export function AddCustomButtons() {
  try {
    return (
      <div className="p-fluid">
        {AddButton(
          "button_PeripheralClock",
          "Peripherals",
          PeripheralButtonClicked
        )}

        {AddButton(
          "button_GenericClock",
          "Generic Clock",
          GenericClockClicked
        )}
      </div>
    );
  } catch (err) {}
}

function AddButton(
  id: string,
  buttonDisplayText: string,
  buttonClick: (arg0: any) => void
) {
  try {
    return (
      <GetButton
        buttonId={id}
        onChange={buttonClick}
        buttonDisplayText={buttonDisplayText}
      />
    );
  } catch (err) {}
}

function PeripheralButtonClicked() {
  callPopUp(GenericPopUp, peripheralClockConfig_PopupHeadding);
}

function GenericClockClicked() {
    callPopUp(GenericPopUp, GenerickClock_PopupHeadding);
  }

function callPopUp(Component: any, action_id: any) {
  const createPopup = React.createElement(Component);
  PopupLoaderId(action_id);
  ReactDOM.render(createPopup, document.querySelector("#popup"));
}
