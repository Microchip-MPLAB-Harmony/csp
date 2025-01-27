
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useContext, useState } from 'react';
import {
    PluginConfigContext,
    useBooleanSymbol,
} from '@mplab_harmony/harmony-plugin-client-lib';

import { ListBox } from 'primereact/listbox';
import ClockGenSelectControllerTemplateBox from './ClockGenSelectControllerTemplateBox';

interface Tab {
    name: string;
    index: string;
    status: string;
}

const generateClkGenTabs = (maxClkGen: number): Tab[] => {
    const refClkTabs: Tab[] = [];
    for (let i = 4; i < maxClkGen; i++) {
        refClkTabs.push({
            name: `CLKGEN ${i}`,
            index: `${i}`,
            status: `clkGen${i}Enable`,
        });
    }
    return refClkTabs;
};

const maxClkGen = 14;
const clkGenTabs = generateClkGenTabs(maxClkGen);


const ClockGenControllerBox = (props: {
    ClkGenControllerData: ControlInterface[];
    cx: (...classNames: string[]) => string;
}) => {
    const { componentId = 'core' } = useContext(PluginConfigContext);
    const [value, setValue] = useState<Tab | null>(clkGenTabs[0]);

    const tabTemplate = (option: any) => {
        // eslint-disable-next-line react-hooks/rules-of-hooks
        const clkGenEnable = useBooleanSymbol({
            componentId,
            symbolId: option.status
        });
        return (
            <div
                style={{ fontSize: '10px' }}
                className={clkGenEnable.value ? props.cx('enable') : props.cx('disable')}>
                {option.name}
            </div>
        );
    };


    return (
        <div>
            <div>
                 <ListBox
                    className={props.cx('clockGenButton')}
                    value={value}
                    options={clkGenTabs}
                    optionLabel='name'
                    itemTemplate={tabTemplate}
                    onChange={(e) => setValue(e.value)}
                /> 
            </div>
            <ClockGenSelectControllerTemplateBox
                index={value?.name ? value.index : '4'}
                ClkGenControllerData={props.ClkGenControllerData}
                componentId={componentId}
                cx={props.cx}
            />
        </div>
    );
};

export default ClockGenControllerBox;