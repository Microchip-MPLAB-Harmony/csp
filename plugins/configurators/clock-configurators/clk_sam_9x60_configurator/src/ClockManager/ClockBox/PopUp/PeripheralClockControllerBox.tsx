import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import {useState } from 'react';
import { Button } from 'primereact/button';
import { Dialog } from 'primereact/dialog';
import PeripheralClockConfiguration from './PeripheralClockConfiguration';

const PeripheralClockControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const [periPheralPopup, setPeriPheralPopup] = useState(false);

  return (
    <div>
      <Button
        label='Peripheral Clock Configuration'
        className={props.cx('periPheralClock')}
        onClick={() => setPeriPheralPopup(true)}
      />
      <Dialog
        header='Peripheral Clock Configuration'
        visible={periPheralPopup}
        maximizable={true}
        onHide={() => {
          setPeriPheralPopup(false);
        }}>
        <PeripheralClockConfiguration />
      </Dialog>
    </div>
  );
};

export default PeripheralClockControllerBox;
