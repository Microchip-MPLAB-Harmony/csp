/*
 * Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
 *
 * Subject to your compliance with these terms, you may use Microchip software
 * and any derivatives exclusively with Microchip products. It is your
 * responsibility to comply with third party license terms applicable to your
 * use of third party software (including open source software) that may
 * accompany Microchip software.
 *
 * THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
 * EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
 * WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
 * PARTICULAR PURPOSE.
 *
 * IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
 * INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
 * WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
 * BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
 * FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
 * ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
 * THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 */
import { Dialog } from 'primereact/dialog';
import { Button } from 'primereact/button';
import GenericClockConfiguration from '../PopUpContent/GenericClockConfiguration';
import PeripheralsConfiguration from '../PopUpContent/PeripheralsConfiguration';
import {
  GenerickClock_PopupHeadding,
  peripheralClockConfig_PopupHeadding,
} from './CustomButtons';
import useForceUpdate from 'use-force-update';
import { SummaryPageHeading } from './CustomButtons';
import SummaryPage from './Summary';

let ActionId: any;
let Width: any;
let Height: any;
export function PopupLoaderId(
  Id: string,
  widthValue: string,
  heightValue: string
) {
  ActionId = Id;
  Width = widthValue;
  Height = heightValue;
  dialogVisibleStatus = true;
}

let dialogVisibleStatus = false;
const GenericPopUp = () => {
  const update = useForceUpdate();

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
            style={{ height: '2.5rem', fontSize: '14px' }}
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
          style={{ width: Width, height: Height, fontSize: '14px' }}
          footer={renderFooter()}
          onHide={() => onHide()}
        >
          <div>
            {ActionId === peripheralClockConfig_PopupHeadding && (
              <PeripheralsConfiguration />
            )}
            {ActionId === GenerickClock_PopupHeadding && (
              <GenericClockConfiguration />
            )}
            {ActionId === SummaryPageHeading && <SummaryPage />}
          </div>
        </Dialog>
      </div>
    </div>
  );
};

export default GenericPopUp;
