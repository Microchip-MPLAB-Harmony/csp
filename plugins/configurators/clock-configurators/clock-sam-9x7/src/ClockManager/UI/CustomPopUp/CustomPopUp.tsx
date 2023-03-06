import { Dialog } from 'primereact/dialog';
import { Button } from 'primereact/button';
import PrimeReact from 'primereact/api';
import {
  peripheralClockConfig_PopupHeadding,
  GenerickClock_PopupHeadding
} from '../MainView/CustomButtons';
import PeripheralsConfiguration from '../PopUpContent/PeripheralsConfiguration';
import GenericClockConfiguration from '../PopUpContent/GenericClockConfiguration';
import { useBetween } from 'use-between';
import useInitService from '../../../InitService';

let dialogVisibleStatus = false;

let ActionId: string;
export function PopupLoaderId(Id: string) {
  dialogVisibleStatus = true;
  ActionId = Id;
}

const GenericPopUp = () => {
  const { refreshScreen } = useBetween(useInitService);

  PrimeReact.ripple = true;

  const onHide = () => {
    dialogVisibleStatus = false;
    refreshScreen();
  };

  const renderHeader = () => {
    return <label>{ActionId}</label>;
  };

  const renderFooter = () => {
    return (
      <div className='flex-row-reverse'>
        <div>
          <Button
            type='button'
            className='p-button-raised p-button-rounded'
            label='Close'
            style={{ height: '2.5rem', fontSize: '14px' }}
            onClick={() => onHide()}
            autoFocus
          />
        </div>
      </div>
    );
  };

  return (
    <div className='dialog-demo'>
      <div className='card'>
        <Dialog
          visible={dialogVisibleStatus}
          maximizable={true}
          closeOnEscape
          closable
          focusOnShow
          modal
          header={renderHeader()}
          footer={renderFooter()}
          onHide={() => onHide()}>
          <div>
            {ActionId === peripheralClockConfig_PopupHeadding && (
              <PeripheralsConfiguration parentUpdate={refreshScreen} />
            )}
            {ActionId === GenerickClock_PopupHeadding && (
              <GenericClockConfiguration parentUpdate={refreshScreen} />
            )}
          </div>
        </Dialog>
      </div>
    </div>
  );
};

export default GenericPopUp;
