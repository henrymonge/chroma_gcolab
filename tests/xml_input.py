monomials={}
monomials['TWO_FLAVOR_EOPREC']='''
    <Name>N_FLAVOR_LOGDET_EVEN_EVEN_FERM_MONOMIAL</Name>
        <FermionAction>
     <FermAct>%(ACTION)s</FermAct>
            <Mass>%(MASS)s</Mass>
            <clovCoeff>%(CLOV_COEFF)s</clovCoeff>
          <FermionBC>
            <FermBC>SIMPLE_FERMBC</FermBC>
            <boundary>1 1 1 -1</boundary>
          </FermionBC>
        </FermionAction>
    <num_flavors>2</num_flavors>
    <NamedObject>
       <monomial_id>%(ID)s_ee</monomial_id>
    </NamedObject>
      </elem>

      <elem>
        <Name>TWO_FLAVOR_EOPREC_CONSTDET_FERM_MONOMIAL</Name>
        <FermionAction>
          <FermAct>%(ACTION)s</FermAct>
            <Mass>%(MASS)s</Mass>
            <clovCoeff>%(CLOV_COEFF)s</clovCoeff>
          <FermState>
           <Name>SIMPLE_FERM_STATE</Name>
           <FermionBC>
            <FermBC>SIMPLE_FERMBC</FermBC>
                 <boundary>1 1 1 -1</boundary>
            </FermionBC>
          </FermState>
        </FermionAction>
            <InvertParam>
              <invType>CG_INVERTER</invType>
              <RsdCG>1.0e-8</RsdCG>
              <MaxCG>1000</MaxCG>
            </InvertParam>
        <ChronologicalPredictor>
        <Name>ZERO_GUESS_4D_PREDICTOR</Name>
        </ChronologicalPredictor>
        <NamedObject>
          <monomial_id>%(ID)s_oo</monomial_id>
        </NamedObject>
      </elem>
'''

monomials['ONE_FLAVOR_EOPREC']='''
      <elem>
        <Name>ONE_FLAVOR_EOPREC_CONSTDET_FERM_RAT_MONOMIAL</Name>
        <num_pf>1</num_pf>
        <Action>
          <FermionAction>
           <FermAct>%(ACTION)s</FermAct>
            <Mass>%(MASS)s</Mass>
            <clovCoeff>%(CLOV_COEFF)s</clovCoeff>
            <FermState>
              <Name>SIMPLE_FERM_STATE</Name>
              <FermionBC>
                <FermBC>SIMPLE_FERMBC</FermBC>
                <boundary>1 1 1 -1</boundary>
              </FermionBC>
            </FermState>
          </FermionAction>
          <ActionApprox>
            <RationalApprox>
              <ratApproxType>READ_COEFFS</ratApproxType>
              <Param>
                <lowerMin>2.0e-4</lowerMin>
                <upperMax>10</upperMax>
                <numPower>-1</numPower>
                <denPower>4</denPower>
                <degree>13</degree>
              </Param>
              <ApproxInfo>
                <lowerMin>0.0002</lowerMin>
                <upperMax>10</upperMax>
                <degree>13</degree>
                <error>8.53359759155053e-09</error>
              </ApproxInfo>
              <PFECoeffs>
                <norm>0.235485866818045</norm>
                <res>0.000225192428610066 0.000493198674487029 0.00101098944690569
                  0.00210966479427735 0.00445341664197467 0.00945108960561729 0.0201221040804977
                  0.0430335164962971 0.0930149163490357 0.206877941073909 0.49800938741062
                  1.50426604429933 9.64588011579469</res>
                <pole>2.13984298644252e-05 0.000167952110725128 0.00060887602643753
                  0.00182959869647478 0.00517440200375724 0.0143300682933111 0.039414086340563
                  0.108339010139494 0.299267597111873 0.840081382951181 2.47015136430147
                  8.35141226703362 47.1440813696294</pole>
              </PFECoeffs>
              <IPFECoeffs>
                <norm>4.24653935079968</norm>
                <res>-1.83558710964104e-06 -9.12204689643441e-06 -3.45205646515825e-05
                  -0.000123982091699911 -0.000439259033038762 -0.0015506886355438
                  -0.00547845322979375 -0.0194658268078658 -0.0703494148580012 -0.266556492901423
                  -1.15339049324629 -7.39500484641764 -208.006767009261</res>
                <pole>4.24231407611734e-05 0.000239480453850279 0.000809666981912087 0.002380721726
                  0.00668298211801512 0.018460571103842 0.0507432795148089 0.139566676101156
                  0.386518093984147 1.0931358903204 3.28474092123776 11.9081563867525
                  93.4648015144787</pole>
              </IPFECoeffs>
            </RationalApprox>
            <InvertParam>
              <invType>CG_INVERTER</invType>
              <RsdCG>1.0e-8</RsdCG>
              <MaxCG>1000</MaxCG>
            </InvertParam>
          </ActionApprox>
          <ForceApprox>
            <RationalApprox>
              <ratApproxType>READ_COEFFS</ratApproxType>
              <Param>
                <lowerMin>2.0e-4</lowerMin>
                <upperMax>10</upperMax>
                <numPower>-1</numPower>
                <denPower>2</denPower>
                <degree>12</degree>
              </Param>
              <ApproxInfo>
                <lowerMin>0.0002</lowerMin>
                <upperMax>10</upperMax>
                <degree>12</degree>
                <error>5.2284680862031e-08</error>
              </ApproxInfo>
              <PFECoeffs>
                <norm>0.0547276831428071</norm>
                <res>0.00507698729668402 0.0066151725685671 0.0101577938592028 0.0167794204884187
                  0.0284928077171634 0.0488808001988765 0.0842952468229152 0.146367448808401
                  0.258625107384016 0.481012357852968 1.04600847097866 3.86723649654098</res>
                <pole>1.51480322230288e-05 0.000165259114300968 0.000661184012887753
                  0.00214955953261573 0.00657190811374048 0.0197043312297316 0.0587640674448055
                  0.175534749714768 0.529999019144126 1.6565878795396 5.78532483906374
                  30.6835527589452</pole>
              </PFECoeffs>
              <IPFECoeffs>
                <norm>18.2722882200328</norm>
                <res>-3.67396011655789e-07 -2.79527600795379e-06 -1.56773360818779e-05
                  -8.23503682881716e-05 -0.000424877064532166 -0.00218335514109711
                  -0.0112605577342041 -0.0590061495274579 -0.324805216795793 -2.07825914676428
                  -21.6648322084522 -1978.96735278723</res>
                <pole>6.51815001904216e-05 0.000345702282177066 0.00120730087712331
                  0.00377359188933919 0.011393755386041 0.0340344037940959 0.101500526796983
                  0.304325618281001 0.930423172586555 3.02487652607464 12.1022069400519
                  132.030350249685</pole>
              </IPFECoeffs>
            </RationalApprox>
            <InvertParam>
              <invType>CG_INVERTER</invType>
              <RsdCG>1.0e-8</RsdCG>
              <MaxCG>1000</MaxCG>
            </InvertParam>
          </ForceApprox>
        </Action>
        <NamedObject>
          <monomial_id>%(ID)s</monomial_id>
        </NamedObject>
      </elem>
'''

monomials['GAUGE_MONOMIAL']='''
      <elem>
    <Name>GAUGE_MONOMIAL</Name>
    <GaugeAction>
       <Name>%(ACTION)s</Name>
       <beta>%(BETA)s</beta>
       <GaugeBC>
        <Name>PERIODIC_GAUGEBC</Name>
           </GaugeBC>
        </GaugeAction>
    <NamedObject>
      <monomial_id>%(ID)s</monomial_id>
        </NamedObject>
      </elem>
'''
integrators={}
integrators['LCM_STS_LEAPFROG']='''
        <Integrator>
          <Name>LCM_STS_LEAPFROG</Name>
          <n_steps>%(NSTEPS)s</n_steps>
           <monomial_ids>
             <elem>HMC::light_ee</elem>
             <elem>HMC::light_oo</elem>
             <elem>HMC::rat_strange</elem>
             <elem>HMC::gauge</elem>
           </monomial_ids>
        </Integrator>
'''