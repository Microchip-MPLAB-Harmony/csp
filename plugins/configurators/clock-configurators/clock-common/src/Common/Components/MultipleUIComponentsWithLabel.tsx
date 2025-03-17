import { useSymbols } from '@mplab_harmony/harmony-plugin-client-lib';
import { ConfigSymbol, DefaultControl } from '@mplab_harmony/harmony-plugin-client-lib';
import React from 'react';
import styled from 'styled-components';

const GridContainer = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  width: 30rem;
`;

const GridItem = styled.div`
  display: flex;
  align-items: center;
`;

const LabelContainer = styled.div`
  justify-content: flex-start;
  max-width: 100%; /* Ensure the label container does not exceed the available space */
  white-space: nowrap; /* Prevent the label from wrapping to the next line */
  overflow: hidden; /* Hide any overflow content */
  text-overflow: ellipsis; /* Display ellipsis (...) for overflow content */
`;

const LabelHidden = styled.div`
  display: none;
`;

const LabelVisible = styled.div`
  display: block;
  opacity: 1;
  transition: opacity 0.3s ease-in-out;
`;

const ComponentHidden = styled.div`
  display: none;
`;

const ComponentVisible = styled.div`
  display: block;
`;

const EmptySpace = styled.div`
  height: 1.5rem;
  visibility: hidden;
`;

const MultipleUIComponentsWithLabel = (props: { componentId: any; symbolsArray: string[] }) => {
  const symbolsArray = useSymbols({
    componentId: props.componentId,
    symbolIds: props.symbolsArray
  }) as ConfigSymbol<any>[];

  return (
    <GridContainer>
      {symbolsArray.map(
        (symbol) =>
          symbol.visible && (
            <React.Fragment key={symbol.symbolId}>
              <GridItem className={symbol.label ? 'label-visible' : 'label-hidden'}>
                <LabelContainer>
                  <label>{symbol.label}</label>
                </LabelContainer>
              </GridItem>
              <GridItem className={symbol.visible ? 'component-visible' : 'component-hidden'}>
                <DefaultControl symbol={symbol} />
              </GridItem>
            </React.Fragment>
          )
      )}
      <GridItem className='empty-space'></GridItem>
    </GridContainer>
  );
};

export default MultipleUIComponentsWithLabel;
