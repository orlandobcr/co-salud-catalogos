   Building co-salud-catalogos @ file:///Users/andresfajardo/Library/Mobile%20Documents/com~apple~CloudDocs/Digitall%20PRO%20SAS/Clientes/DigitALL%20PRO/cac-salud-catalogos
      Built co-salud-catalogos @ file:///Users/andresfajardo/Library/Mobile%20Documents/com~apple~CloudDocs/Digitall%20PRO%20SAS/Clientes/DigitALL%20PRO/cac-salud-catalogos
Installed 1 package in 1ms
# Inventario de fuentes y esquemas

Generado a partir de los catálogos sincronizados en `catalogos_co/co/`.
Cada catálogo trae metadata reproducible (URL fuente, versión, sha256, fecha de sync).

**Cómo regenerar este inventario:**
```bash
python docs/build_inventario.py > docs/inventario_fuentes.md
```

---

## Resumen

| Catálogo | Kind | Filas | Tamaño | URL fuente |
|----------|------|------:|-------:|------------|
| `eapb_codigos` | `sispro_aspx` | 1,717 | 1.3 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CodigoEAPByNit> |
| `ips_listado_nivel` | `socrata` | 11,466 | 8.9 MB | <https://www.datos.gov.co/resource/ugc5-acjp.json> |
| `ips_por_nivel` | `socrata` | 41,427 | 35.3 MB | <https://www.datos.gov.co/resource/s2ru-bqt6.json> |
| `reps_capacidades` | `reps_export` | 97,136 | 102.0 MB | <https://prestadores.minsalud.gov.co/habilitacion/consultas/capacidadesinstaladas_reps.aspx> |
| `reps_habilitados` | `reps_export` | 60,828 | 72.8 MB | <https://prestadores.minsalud.gov.co/habilitacion/consultas/habilitados_reps.aspx> |
| `reps_medidas_seguridad` | `reps_export` | 3,443 | 4.8 MB | <https://prestadores.minsalud.gov.co/habilitacion/consultas/medidasseguridad_reps.aspx> |
| `reps_prestadores` | `socrata` | 76,821 | 74.2 MB | <https://www.datos.gov.co/resource/c36g-9fc2.json> |
| `reps_sanciones` | `reps_export` | 788 | 1.1 MB | <https://prestadores.minsalud.gov.co/habilitacion/consultas/sanciones_reps.aspx> |
| `reps_sedes` | `reps_export` | 76,561 | 117.4 MB | <https://prestadores.minsalud.gov.co/habilitacion/consultas/sedes_reps.aspx> |
| `reps_servicios` | `reps_export` | 228,293 | 854.9 MB | <https://prestadores.minsalud.gov.co/habilitacion/consultas/serviciossedes_reps.aspx> |
| `servicios_habilitados` | `socrata` | 1,859 | 1.4 MB | <https://www.datos.gov.co/resource/p9n2-9qsb.json> |
| `sispro_cod_eapbrnse` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CodEAPBRNSE> |
| `sispro_cod_sede_ips_demo` | `sispro_aspx` | 223 | 141.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CodSedeIPSDemo> |
| `sispro_cpti_peligros_condicionesde_seguridad` | `sispro_aspx` | 12 | 8.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIPeligrosCondicionesdeSeguridad> |
| `sispro_entidades_pma140_gipm` | `sispro_aspx` | 1,274 | 777.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EntidadesPMA140GIPM> |
| `sispro_entidades_pts` | `sispro_aspx` | 280 | 233.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EntidadesPTS> |
| `sispro_fne_subtipo_entidad` | `sispro_aspx` | 28 | 17.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNESubtipoEntidad> |
| `sispro_ind_uso_entidad_en_sac` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IndUsoEntidadEnSAC> |
| `sispro_ips_sub_red` | `sispro_aspx` | 24 | 15.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IPSSubRed> |
| `sispro_lce_entidades_poblacion_elegible_subsidia_salud2_na` | `sispro_aspx` | 9 | 7.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LCEEntidadesPoblacionElegibleSubsidiaSalud2NA> |
| `sispro_rmips_no_reps` | `sispro_aspx` | 1 | 1.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RMIPSNoREPS> |
| `sispro_rua_codigo_entidad_supervivencia` | `sispro_aspx` | 456 | 307.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RUACodigoEntidadSupervivencia> |
| `sispro_sac_tipo_entidad` | `sispro_aspx` | 4 | 2.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACTipoEntidad> |
| `sispro_sacip_sy_eps_svalidasx_fepa` | `sispro_aspx` | 22 | 14.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACIPSyEPSSvalidasxFEPA> |
| `cie10` | `sispro_aspx` | 14,000 | 10.8 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CIE10> |
| `cups` | `sispro_aspx` | 12,000 | 9.6 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CUPS> |
| `glosario_medico` | `socrata` | 900 | 502.8 KB | <https://www.datos.gov.co/resource/98ms-bv6s.json> |
| `ium_medicamentos` | `sispro_aspx` | 36,000 | 33.4 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IUM> |
| `medicamentos_pbs` | `socrata` | 2,067 | 1.6 MB | <https://www.datos.gov.co/resource/jtqe-tuvf.json> |
| `procedimientos_pbs` | `socrata` | 8,114 | 9.8 MB | <https://www.datos.gov.co/resource/9zcz-bjue.json> |
| `sispro_aco_tipo_soporte_documental` | `sispro_aspx` | 6 | 4.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOTipoSoporteDocumental> |
| `sispro_aps_acceso_vivienda` | `sispro_aspx` | 5 | 3.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSAccesoVivienda> |
| `sispro_aps_accion_intersectorial` | `sispro_aspx` | 9 | 6.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSAccionIntersectorial> |
| `sispro_aps_agente_medicina` | `sispro_aspx` | 4 | 2.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSAgenteMedicina> |
| `sispro_aps_animales` | `sispro_aspx` | 13 | 8.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSAnimales> |
| `sispro_aps_diagnostico_nutricion` | `sispro_aspx` | 7 | 4.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSDiagnosticoNutricion> |
| `sispro_aps_disposicion_residuos` | `sispro_aspx` | 6 | 4.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSDisposicionResiduos> |
| `sispro_aps_ecomapa` | `sispro_aspx` | 5 | 3.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSEcomapa> |
| `sispro_aps_enfermedad_transmisible` | `sispro_aspx` | 8 | 5.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSEnfermedadTransmisible> |
| `sispro_aps_excreta` | `sispro_aspx` | 8 | 5.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSExcreta> |
| `sispro_apsapgar` | `sispro_aspx` | 4 | 2.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSAPGAR> |
| `sispro_area_covid` | `sispro_aspx` | 2 | 1.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=AreaCovid> |
| `sispro_catalogo_cu_ms` | `sispro_aspx` | 164,000 | 149.9 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CatalogoCUMs> |
| `sispro_categoria_medicamento` | `sispro_aspx` | 7 | 4.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CategoriaMedicamento> |
| `sispro_clasificacion_atc` | `sispro_aspx` | 6,000 | 3.6 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ClasificacionATC> |
| `sispro_cups04y05` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CUPS04y05> |
| `sispro_cups_anterior` | `sispro_aspx` | 12,000 | 8.6 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CUPSAnterior> |
| `sispro_cups_gr_servicios` | `sispro_aspx` | 1,444,000 | 855.0 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CUPSGrServicios> |
| `sispro_cups_rips` | `sispro_aspx` | 14,000 | 10.2 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CUPSRips> |
| `sispro_cupscie` | `sispro_aspx` | 1,581 | 1.2 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CUPSCIE> |
| `sispro_dispositivos_medicos` | `sispro_aspx` | 21 | 15.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DispositivosMedicos> |
| `sispro_dispositivos_medicos_libertad_vigilada` | `sispro_aspx` | 8,000 | 7.7 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DispositivosMedicosLibertadVigilada> |
| `sispro_dmes_categoria_reactivo` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESCategoriaReactivo> |
| `sispro_dmes_presentacion_comercial` | `sispro_aspx` | 131 | 77.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESPresentacionComercial> |
| `sispro_enfermedad_huerfana` | `sispro_aspx` | 4,000 | 2.6 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EnfermedadHuerfana> |
| `sispro_entidad_financiera_nit` | `sispro_aspx` | 24 | 15.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EntidadFinancieraNit> |
| `sispro_estado_registro_sanitario` | `sispro_aspx` | 10 | 6.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EstadoRegistroSanitario> |
| `sispro_finalidad_cups` | `sispro_aspx` | 990 | 591.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FinalidadCUPS> |
| `sispro_forma_farmaceutica` | `sispro_aspx` | 61 | 36.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FormaFarmaceutica> |
| `sispro_medicamentos_dci` | `sispro_aspx` | 16,000 | 9.7 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=MedicamentosDCI> |
| `sispro_pagos_covid19_unilateral` | `sispro_aspx` | 231 | 181.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PagosCOVID19Unilateral> |
| `sispro_pai_mecanismo_vacuna` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PAIMecanismoVacuna> |
| `sispro_productos_nutricionales` | `sispro_aspx` | 314 | 222.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ProductosNutricionales> |
| `sispro_red_servicios_thscovid` | `sispro_aspx` | 226 | 142.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RedServiciosTHSCOVID> |
| `sispro_rlcpd_actividades_cuidado` | `sispro_aspx` | 19 | 13.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDActividadesCuidado> |
| `sispro_rlcpd_barreras_lugar` | `sispro_aspx` | 9 | 6.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDBarrerasLugar> |
| `sispro_rlcpd_clase_adecuaciones` | `sispro_aspx` | 5 | 4.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDClaseAdecuaciones> |
| `sispro_rlcpd_consecuencias_negativas` | `sispro_aspx` | 11 | 7.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDConsecuenciasNegativas> |
| `sispro_rlcpd_efectos_positivos` | `sispro_aspx` | 5 | 3.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDEfectosPositivos> |
| `sispro_rlcpd_horas_autocuidado` | `sispro_aspx` | 3 | 2.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDHorasAutocuidado> |
| `sispro_rlcpd_horas_cuidado` | `sispro_aspx` | 4 | 3.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDHorasCuidado> |
| `sispro_ser_tipo_documento_soporte` | `sispro_aspx` | 16 | 11.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SERTipoDocumentoSoporte> |
| `sispro_tipo_medicamento_pos` | `sispro_aspx` | 2 | 1.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoMedicamentoPOS> |
| `sispro_tipo_producto_nutricional` | `sispro_aspx` | 22 | 16.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoProductoNutricional> |
| `sispro_tipo_programa_salud_covid` | `sispro_aspx` | 5 | 3.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoProgramaSaludCOVID> |
| `sispro_tv_sociedad_cientifica` | `sispro_aspx` | 110 | 68.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TVSociedadCientifica> |
| `sispro_estado_evolucion` | `sispro_aspx` | 9 | 6.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EstadoEvolucion> |
| `sispro_finalidad_sexo_edad` | `sispro_aspx` | 34 | 22.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FinalidadSexoEdad> |
| `sispro_unirs` | `sispro_aspx` | 915 | 735.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=UNIRS> |
| `sispro_aco_ciiu` | `sispro_aspx` | 8 | 5.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOCiiu> |
| `sispro_aco_entidad_autorizada` | `sispro_aspx` | 203 | 174.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOEntidadAutorizada> |
| `sispro_aco_tipo_entidad` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOTipoEntidad> |
| `sispro_aco_tipo_entidad_reserva` | `sispro_aspx` | 2 | 1.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOTipoEntidadReserva> |
| `sispro_aco_tipo_persona` | `sispro_aspx` | 3 | 2.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOTipoPersona> |
| `sispro_aco_tipo_producto` | `sispro_aspx` | 6 | 4.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOTipoProducto> |
| `sispro_aco_tipo_soporte_seguimiento` | `sispro_aspx` | 6 | 4.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOTipoSoporteSeguimiento> |
| `sispro_afp` | `sispro_aspx` | 16 | 10.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=AFP> |
| `sispro_arl` | `sispro_aspx` | 10 | 6.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ARL> |
| `sispro_arl_estado_pago` | `sispro_aspx` | 4 | 3.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ARLEstadoPago> |
| `sispro_arl_tipo_aportante` | `sispro_aspx` | 11 | 7.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ARLTipoAportante> |
| `sispro_ccf_estado_pago` | `sispro_aspx` | 2 | 1.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CCFEstadoPago> |
| `sispro_cma_indicador_registro_sustitucion` | `sispro_aspx` | 2 | 1.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMAIndicadorRegistroSustitucion> |
| `sispro_cma_modalidad_subsidio` | `sispro_aspx` | 3 | 2.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMAModalidadSubsidio> |
| `sispro_cma_novedad` | `sispro_aspx` | 3 | 2.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMANovedad> |
| `sispro_cma_sistema_pago` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMASistemaPago> |
| `sispro_cma_tipo_cuenta_bancaria` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMATipoCuentaBancaria> |
| `sispro_cma_tipo_cuenta_maestra` | `sispro_aspx` | 6 | 4.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMATipoCuentaMaestra> |
| `sispro_cma_tipo_movimiento` | `sispro_aspx` | 5 | 3.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMATipoMovimiento> |
| `sispro_cmh_tipo_cuenta_maestra` | `sispro_aspx` | 24 | 15.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMHTipoCuentaMaestra> |
| `sispro_cmh_tipo_movimiento` | `sispro_aspx` | 7 | 4.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMHTipoMovimiento> |
| `sispro_cmh_tipo_movimiento_pg` | `sispro_aspx` | 22 | 14.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMHTipoMovimientoPG> |
| `sispro_cmr_sistema_pago` | `sispro_aspx` | 4 | 2.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMRSistemaPago> |
| `sispro_cmr_tipo_cuenta_maestra` | `sispro_aspx` | 2 | 1.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMRTipoCuentaMaestra> |
| `sispro_cmv_tipo_movimiento` | `sispro_aspx` | 13 | 8.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMVTipoMovimiento> |
| `sispro_eam_entidad_seguimiento` | `sispro_aspx` | 6 | 4.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EAMEntidadSeguimiento> |
| `sispro_eam_jornada_atencion` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EAMJornadaAtencion> |
| `sispro_eam_nivel_ejecucion` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EAMNivelEjecucion> |
| `sispro_eam_razon_no_ejecucion` | `sispro_aspx` | 3 | 2.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EAMRazonNoEjecucion> |
| `sispro_estado_recobro` | `sispro_aspx` | 4 | 2.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EstadoRecobro> |
| `sispro_factura_sin_contrato` | `sispro_aspx` | 6 | 5.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=facturaSinContrato> |
| `sispro_incapacidades_causal_contingencia` | `sispro_aspx` | 5 | 3.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesCausalContingencia> |
| `sispro_incapacidades_causal_dias_no_pagados` | `sispro_aspx` | 2 | 1.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesCausalDiasNoPagados> |
| `sispro_incapacidades_causal_glosa` | `sispro_aspx` | 12 | 8.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesCausalGlosa> |
| `sispro_incapacidades_concepto_rehabilitacion` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesConceptoRehabilitacion> |
| `sispro_incapacidades_estado_pago` | `sispro_aspx` | 3 | 2.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesEstadoPago> |
| `sispro_incapacidades_grupos_servicios` | `sispro_aspx` | 5 | 3.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesGruposServicios> |
| `sispro_incapacidades_motivo_retroactividad` | `sispro_aspx` | 4 | 3.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesMotivoRetroactividad> |
| `sispro_incapacidades_profesional_pcl` | `sispro_aspx` | 2 | 1.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesProfesionalPCL> |
| `sispro_incapacidades_tipo_evento_laboral` | `sispro_aspx` | 2 | 1.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesTipoEventoLaboral> |
| `sispro_incapacidades_tipo_pago` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesTipoPago> |
| `sispro_pila_causal_no_pago_electronico` | `sispro_aspx` | 4 | 3.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILACausalNoPagoElectronico> |
| `sispro_pila_correcciones` | `sispro_aspx` | 2 | 1.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILACorrecciones> |
| `sispro_pila_cruce_personas` | `sispro_aspx` | 9 | 6.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILACrucePersonas> |
| `sispro_pila_forma_presentacion` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILAFormaPresentacion> |
| `sispro_pila_identificador` | `sispro_aspx` | 2 | 1.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILAIdentificador> |
| `sispro_pila_indicador_decreto688` | `sispro_aspx` | 2 | 1.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILAIndicadorDecreto688> |
| `sispro_pila_indicador_tarifa_especial_pensiones` | `sispro_aspx` | 4 | 3.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILAIndicadorTarifaEspecialPensiones> |
| `sispro_pila_ingreso` | `sispro_aspx` | 3 | 2.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILAIngreso> |
| `sispro_pila_modalidad_planilla` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILAModalidadPlanilla> |
| `sispro_pila_retiro` | `sispro_aspx` | 4 | 2.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILARetiro> |
| `sispro_rec_ambito_atencion` | `sispro_aspx` | 5 | 3.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECAmbitoAtencion> |
| `sispro_rec_causa_negacion` | `sispro_aspx` | 40 | 27.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECCausaNegacion> |
| `sispro_rec_causa_no_entrega` | `sispro_aspx` | 16 | 10.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECCausaNoEntrega> |
| `sispro_rec_codigo_servicio_no_financiado` | `sispro_aspx` | 55 | 36.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECCodigoServicioNoFinanciado> |
| `sispro_rec_concepto_negacion_servicio` | `sispro_aspx` | 2 | 1.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECConceptoNegacionServicio> |
| `sispro_rec_motivo_neg_ctc` | `sispro_aspx` | 10 | 7.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECMotivoNegCTC> |
| `sispro_rec_motivo_ntr_ctc` | `sispro_aspx` | 8 | 6.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECMotivoNtrCTC> |
| `sispro_rec_servicios_especificos_no_pos` | `sispro_aspx` | 12 | 8.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECServiciosEspecificosNoPos> |
| `sispro_rec_tipo_servicio` | `sispro_aspx` | 6 | 4.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECTipoServicio> |
| `sispro_sgd01221` | `sispro_aspx` | 4 | 2.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGD01221> |
| `sispro_sgd012321` | `sispro_aspx` | 5 | 3.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGD012321> |
| `sispro_sgd034521` | `sispro_aspx` | 5 | 3.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGD034521> |
| `sispro_sgd045621` | `sispro_aspx` | 5 | 3.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGD045621> |
| `sispro_sgd067891021` | `sispro_aspx` | 7 | 4.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGD067891021> |
| `sispro_sgd1221` | `sispro_aspx` | 3 | 2.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGD1221> |
| `sispro_sgd_actividad` | `sispro_aspx` | 70 | 44.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGDActividad> |
| `sispro_sgd_actividades_nomin` | `sispro_aspx` | 73 | 47.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGDActividadesNomin> |
| `sispro_sgd_ambito_prestacion` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGDAmbitoPrestacion> |
| `sispro_sgd_baciloscopia_diag` | `sispro_aspx` | 6 | 4.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGDBaciloscopiaDiag> |
| `sispro_sgd_cal_muestra_cit_cer` | `sispro_aspx` | 6 | 4.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGDCalMuestraCitCer> |
| `sispro_siem_causa_entrega_incompleta` | `sispro_aspx` | 7 | 5.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SIEMCausaEntregaIncompleta> |
| `sispro_siem_causa_no_entrega` | `sispro_aspx` | 2 | 2.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SIEMCausaNoEntrega> |
| `sispro_siem_profesion_quien_entrega` | `sispro_aspx` | 3 | 2.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SIEMProfesionQuienEntrega> |
| `sispro_siem_sitio_entrega` | `sispro_aspx` | 4 | 3.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SIEMSitioEntrega> |
| `sispro_siem_via_autorizacion_entrega` | `sispro_aspx` | 4 | 3.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SIEMViaAutorizacionEntrega> |
| `sispro_tipo_recobro` | `sispro_aspx` | 2 | 1.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoRecobro> |
| `sispro_cobertura_plan` | `sispro_aspx` | 15 | 10.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=coberturaPlan> |
| `sispro_cobertura_plan_usuario` | `sispro_aspx` | 24 | 15.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CoberturaPlanUsuario> |
| `sispro_cpti_tipo_poblacion` | `sispro_aspx` | 5 | 3.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTITipoPoblacion> |
| `sispro_eps_volumen_afiliados` | `sispro_aspx` | 103 | 63.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EPSVolumenAfiliados> |
| `sispro_etnia` | `sispro_aspx` | 6 | 4.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Etnia> |
| `sispro_lce_novedad_eliminacion` | `sispro_aspx` | 44 | 31.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LCENovedadEliminacion> |
| `sispro_lce_responsables_envio_informacion_por_tipo_poblacion_especial` | `sispro_aspx` | 42 | 37.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LCEResponsablesEnvioInformacionPorTipoPoblacionEspecial> |
| `sispro_lce_tipo_poblacion_especial` | `sispro_aspx` | 21 | 15.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LCETipoPoblacionEspecial> |
| `sispro_orientacion_sexual` | `sispro_aspx` | 5 | 3.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=OrientacionSexual> |
| `sispro_pai_tipo_id_nacido_vivo` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PAITipoIDNacidoVivo> |
| `sispro_pro170_regimen_salud` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PRO170RegimenSalud> |
| `sispro_psracausretivincbenef` | `sispro_aspx` | 6 | 4.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRACAUSRETIVINCBENEF> |
| `sispro_psraestadobenefi` | `sispro_aspx` | 6 | 4.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRAESTADOBENEFI> |
| `sispro_psratipobenefi` | `sispro_aspx` | 13 | 8.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRATIPOBENEFI> |
| `sispro_psratiposubsid` | `sispro_aspx` | 5 | 3.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRATIPOSUBSID> |
| `sispro_psrccausretiafil` | `sispro_aspx` | 13 | 8.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRCCAUSRETIAFIL> |
| `sispro_psrccondbeneccf` | `sispro_aspx` | 2 | 1.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRCCONDBENECCF> |
| `sispro_psrcestaafilccf` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRCESTAAFILCCF> |
| `sispro_psrcestadobenefi` | `sispro_aspx` | 5 | 3.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRCESTADOBENEFI> |
| `sispro_psrctipmiepobcub` | `sispro_aspx` | 3 | 2.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRCTIPMIEPOBCUB> |
| `sispro_psrctipoafilccf` | `sispro_aspx` | 7 | 4.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRCTIPOAFILCCF> |
| `sispro_riba_actividad_economica` | `sispro_aspx` | 17 | 11.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBAActividadEconomica> |
| `sispro_riba_nivel_educativo` | `sispro_aspx` | 6 | 4.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBANivelEducativo> |
| `sispro_riba_nivel_sisben` | `sispro_aspx` | 4 | 2.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBANivelSISBEN> |
| `sispro_riba_novedad_ingreso_modificacion` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBANovedadIngresoModificacion> |
| `sispro_riba_parentesco_cotizante` | `sispro_aspx` | 8 | 5.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBAParentescoCotizante> |
| `sispro_riba_tipo_afiliado` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBATipoAfiliado> |
| `sispro_riba_tipo_cotizante` | `sispro_aspx` | 4 | 3.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBATipoCotizante> |
| `sispro_riba_tipo_vivienda` | `sispro_aspx` | 4 | 2.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBATipoVivienda> |
| `sispro_saa_tipo_novedad` | `sispro_aspx` | 18 | 11.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SAATipoNovedad> |
| `sispro_tenencia_hogar` | `sispro_aspx` | 5 | 3.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TenenciaHogar> |
| `sispro_tipo_entidad_giro_subsidiado` | `sispro_aspx` | 2 | 1.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoEntidadGiroSubsidiado> |
| `sispro_tipo_entidad_reporta_incapacidad` | `sispro_aspx` | 4 | 3.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoEntidadReportaIncapacidad> |
| `sispro_tipo_estandar_id_internacional` | `sispro_aspx` | 5 | 3.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoEstandarIDInternacional> |
| `sispro_tipo_estandar_para_cantidad_y_unidad_medida` | `sispro_aspx` | 33 | 24.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoEstandarParaCantidadYUnidadMedida> |
| `sispro_tipo_id_afiliado_rs` | `sispro_aspx` | 11 | 7.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDAfiliadoRS> |
| `sispro_tipo_id_aportante` | `sispro_aspx` | 9 | 6.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDAportante> |
| `sispro_tipo_id_cotizante` | `sispro_aspx` | 6 | 4.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDCotizante> |
| `sispro_tipo_id_demo` | `sispro_aspx` | 2 | 1.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIdDemo> |
| `sispro_tipo_id_empleador` | `sispro_aspx` | 5 | 3.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDEmpleador> |
| `sispro_tipo_id_sisdis` | `sispro_aspx` | 5 | 3.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIdSISDIS> |
| `sispro_tipo_idrccnms` | `sispro_aspx` | 5 | 3.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDRCCNMS> |
| `sispro_tipo_idrcpa` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDRCPA> |
| `sispro_tipo_idrctipa` | `sispro_aspx` | 4 | 2.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDRCTIPA> |
| `sispro_tipo_incapacidad` | `sispro_aspx` | 5 | 3.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIncapacidad> |
| `sispro_tipo_personal` | `sispro_aspx` | 61 | 37.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoPersonal> |
| `sispro_tipo_salario_afiliado` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoSalarioAfiliado> |
| `sispro_tipologia_ebs` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipologiaEBS> |
| `codigos_postales` | `socrata` | 3,681 | 2.2 MB | <https://www.datos.gov.co/resource/ixig-z8b5.json> |
| `divipola_centros_poblados` | `socrata` | 8,161 | 2.7 MB | <https://www.datos.gov.co/resource/xaxy-8nri.json> |
| `divipola_departamentos` | `socrata` | 33 | 5.6 KB | <https://www.datos.gov.co/resource/vcjz-niiq.json> |
| `divipola_municipios` | `socrata` | 1,122 | 240.5 KB | <https://www.datos.gov.co/resource/gdxc-w37w.json> |
| `sispro_dmes_pais` | `sispro_aspx` | 249 | 146.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESPais> |
| `vias_invias` | `socrata` | 710 | 589.3 MB | <https://www.datos.gov.co/resource/ie7y-asdn.json> |
| `sispro_administradora_recuado_resolucion1715de2014` | `sispro_aspx` | 3 | 2.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=AdministradoraRecuadoResolucion1715de2014> |
| `sispro_anexo_tecnico_nombre` | `sispro_aspx` | 255 | 174.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=AnexoTecnicoNombre> |
| `sispro_aplicacion` | `sispro_aspx` | 35 | 25.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Aplicacion> |
| `sispro_asegurador_demo` | `sispro_aspx` | 37 | 23.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=AseguradorDemo> |
| `sispro_campo_tabla_referencia` | `sispro_aspx` | 13 | 9.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CampoTablaReferencia> |
| `sispro_cargo_dir_docentes` | `sispro_aspx` | 6 | 4.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CargoDirDocentes> |
| `sispro_cargo_docente` | `sispro_aspx` | 9 | 5.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CargoDocente> |
| `sispro_cargos_administrativos_edu` | `sispro_aspx` | 7 | 4.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CargosAdministrativosEdu> |
| `sispro_cargos_apoyo_edu` | `sispro_aspx` | 13 | 8.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CargosApoyoEdu> |
| `sispro_catalogo_expedientes_sismed` | `sispro_aspx` | 46,000 | 35.3 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CatalogoExpedientesSISMED> |
| `sispro_causal_no_pago` | `sispro_aspx` | 12 | 8.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CausalNoPago> |
| `sispro_clase_triage` | `sispro_aspx` | 5 | 3.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ClaseTriage> |
| `sispro_codigo_prepagadas` | `sispro_aspx` | 11 | 7.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CodigoPrepagadas> |
| `sispro_comodin0` | `sispro_aspx` | 1 | 1.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Comodin0> |
| `sispro_comodin00` | `sispro_aspx` | 1 | 1.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Comodin00> |
| `sispro_comodin000` | `sispro_aspx` | 1 | 1.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Comodin000> |
| `sispro_comodin9999` | `sispro_aspx` | 2 | 1.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Comodin9999> |
| `sispro_con_victima` | `sispro_aspx` | 6 | 4.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ConVictima> |
| `sispro_concepto_recaudo` | `sispro_aspx` | 5 | 3.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=conceptoRecaudo> |
| `sispro_condicion_beneficiario` | `sispro_aspx` | 2 | 1.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CondicionBeneficiario> |
| `sispro_condicion_luz` | `sispro_aspx` | 2 | 1.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CondicionLuz> |
| `sispro_cpti_actividad_economica` | `sispro_aspx` | 21 | 15.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIActividadEconomica> |
| `sispro_cpti_frecuencia` | `sispro_aspx` | 5 | 3.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIFrecuencia> |
| `sispro_cpti_nivel_escolar` | `sispro_aspx` | 12 | 8.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTINivelEscolar> |
| `sispro_cpti_peligros_biologicos` | `sispro_aspx` | 10 | 7.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIPeligrosBiologicos> |
| `sispro_cpti_peligros_biomecanicos` | `sispro_aspx` | 5 | 3.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIPeligrosBiomecanicos> |
| `sispro_cpti_peligros_fisicos` | `sispro_aspx` | 8 | 5.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIPeligrosFisicos> |
| `sispro_cpti_peligros_psicosociales` | `sispro_aspx` | 10 | 7.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIPeligrosPsicosociales> |
| `sispro_cpti_peligros_quimicos` | `sispro_aspx` | 5 | 3.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIPeligrosQuimicos> |
| `sispro_ctr` | `sispro_aspx` | 23 | 14.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CTR> |
| `sispro_dci` | `sispro_aspx` | 10,000 | 5.6 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DCI> |
| `sispro_dis_rol_reportante` | `sispro_aspx` | 3 | 2.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DISRolReportante> |
| `sispro_dis_tipo_transaccion` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DISTipoTransaccion> |
| `sispro_dispersion_geografica` | `sispro_aspx` | 5 | 3.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DispersionGeografica> |
| `sispro_dmes_clasificacion_riesgo` | `sispro_aspx` | 4 | 2.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESClasificacionRiesgo> |
| `sispro_dmes_condicion_almacenamiento` | `sispro_aspx` | 12 | 7.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESCondicionAlmacenamiento> |
| `sispro_dmes_condicion_empaque` | `sispro_aspx` | 14 | 9.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESCondicionEmpaque> |
| `sispro_dmes_unidad_consumo` | `sispro_aspx` | 131 | 76.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESUnidadConsumo> |
| `sispro_eps_pm` | `sispro_aspx` | 110 | 66.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EPS_PM> |
| `sispro_eps_sy_liquidadas` | `sispro_aspx` | 78 | 46.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EPSSyLiquidadas> |
| `sispro_epsc` | `sispro_aspx` | 55 | 35.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EPSC> |
| `sispro_epss` | `sispro_aspx` | 55 | 35.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EPSS> |
| `sispro_esquema_anexo_tecnico` | `sispro_aspx` | 237 | 225.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ESQUEMAAnexoTecnico> |
| `sispro_expresion_regular` | `sispro_aspx` | 106 | 78.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ExpresionRegular> |
| `sispro_ffm` | `sispro_aspx` | 47 | 50.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FFM> |
| `sispro_fne_direccion` | `sispro_aspx` | 121 | 70.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNEDireccion> |
| `sispro_fne_link_validacion` | `sispro_aspx` | 7 | 5.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNELinkValidacion> |
| `sispro_fne_listas_jife` | `sispro_aspx` | 11 | 7.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNEListasJife> |
| `sispro_fne_modalidad_inscripcion` | `sispro_aspx` | 14 | 9.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNEModalidadInscripcion> |
| `sispro_fne_naturaleza_juridica` | `sispro_aspx` | 7 | 4.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNENaturalezaJuridica> |
| `sispro_fne_profesiones` | `sispro_aspx` | 28 | 16.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNEProfesiones> |
| `sispro_fne_rol_tercero` | `sispro_aspx` | 7 | 4.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNERolTercero> |
| `sispro_fne_tipo_proceso_act` | `sispro_aspx` | 17 | 10.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNETipoProcesoAct> |
| `sispro_fne_tipo_producto_importar` | `sispro_aspx` | 3 | 2.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNETipoProductoImportar> |
| `sispro_forma_comercializacion` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FormaComercializacion> |
| `sispro_forma_contratacion_subsidiado` | `sispro_aspx` | 4 | 3.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FormaContratacionSubsidiado> |
| `sispro_franja` | `sispro_aspx` | 3 | 2.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Franja> |
| `sispro_fuente_anexo_tecnico` | `sispro_aspx` | 65 | 41.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FUENTEAnexoTecnico> |
| `sispro_fuente_financiacion` | `sispro_aspx` | 8 | 5.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FuenteFinanciacion> |
| `sispro_grupo_riesgo_capo` | `sispro_aspx` | 17 | 11.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=GrupoRiesgoCAPO> |
| `sispro_indicador_muestra_medica` | `sispro_aspx` | 9 | 6.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IndicadorMuestraMedica> |
| `sispro_institucion_educacion_superior_snies` | `sispro_aspx` | 218 | 172.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=InstitucionEducacionSuperiorSNIES> |
| `sispro_institucion_formacion_trabajoy_desarrollo_humano_siet` | `sispro_aspx` | 716 | 516.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=InstitucionFormacionTrabajoyDesarrolloHumanoSIET> |
| `sispro_instituto_nacional_medicina_legal` | `sispro_aspx` | 332 | 218.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=InstitutoNacionalMedicinaLegal> |
| `sispro_laboratorio_salud_publica` | `sispro_aspx` | 33 | 21.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LaboratorioSaludPublica> |
| `sispro_lc_elegible` | `sispro_aspx` | 3 | 2.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LCElegible> |
| `sispro_lc_nuevo_estado` | `sispro_aspx` | 3 | 2.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LCNuevoEstado> |
| `sispro_min_salud_area_funcional` | `sispro_aspx` | 5 | 3.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=MinSaludAreaFuncional> |
| `sispro_pai_estado_fallecido` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PAIEstadoFallecido> |
| `sispro_pais1` | `sispro_aspx` | 250 | 145.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Pais1> |
| `sispro_pase_componentes` | `sispro_aspx` | 12 | 8.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PASEComponentes> |
| `sispro_pase_dimension` | `sispro_aspx` | 5 | 3.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PASEDimension> |
| `sispro_pase_sub_componentes` | `sispro_aspx` | 41 | 29.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PASESubComponentes> |
| `sispro_pdsp_areas_observacion` | `sispro_aspx` | 71 | 53.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPAreasObservacion> |
| `sispro_pdsp_categoria_fuente_financiacion` | `sispro_aspx` | 52 | 40.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPCategoriaFuenteFinanciacion> |
| `sispro_pdsp_categoria_linea_operativa` | `sispro_aspx` | 43 | 30.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPCategoriaLineaOperativa> |
| `sispro_pdsp_componente` | `sispro_aspx` | 25 | 17.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPComponente> |
| `sispro_pdsp_dimension` | `sispro_aspx` | 10 | 7.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPDimension> |
| `sispro_pdsp_estrategias` | `sispro_aspx` | 417 | 592.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPEstrategias> |
| `sispro_pdsp_fuentes_financiacion` | `sispro_aspx` | 7 | 5.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPFuentesFinanciacion> |
| `sispro_perfil_contratista` | `sispro_aspx` | 29 | 17.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PerfilContratista> |
| `sispro_perfil_por_aplicacion` | `sispro_aspx` | 23 | 16.2 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PerfilPorAplicacion> |
| `sispro_ppss_eje_linea` | `sispro_aspx` | 33 | 24.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PPSSEjeLinea> |
| `sispro_ppss_poblacion_objetivo` | `sispro_aspx` | 26 | 16.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PPSSPoblacionObjetivo> |
| `sispro_ppss_tipo_recurso` | `sispro_aspx` | 10 | 6.4 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PPSSTipoRecurso> |
| `sispro_precio_maximo_med_v2` | `sispro_aspx` | 78,000 | 64.3 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PrecioMaximoMED_V2> |
| `sispro_pro170_causa_levan` | `sispro_aspx` | 4 | 3.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PRO170CausaLevan> |
| `sispro_pro170_fase_implementacion` | `sispro_aspx` | 4 | 3.0 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PRO170FaseImplementacion> |
| `sispro_pro170_tipo_beneficiario` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PRO170TipoBeneficiario> |
| `sispro_pro170_tipo_medida` | `sispro_aspx` | 3 | 2.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PRO170TipoMedida> |
| `sispro_programa_educacion_siet` | `sispro_aspx` | 4,000 | 3.3 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ProgramaEducacionSIET> |
| `sispro_programa_educacion_superior_snies` | `sispro_aspx` | 4,000 | 3.3 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ProgramaEducacionSuperiorSNIES> |
| `sispro_pss_excepcion` | `sispro_aspx` | 54 | 45.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSSExcepcion> |
| `sispro_resguardo_nit` | `sispro_aspx` | 13 | 8.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ResguardoNit> |
| `sispro_sac_etapa_proceso` | `sispro_aspx` | 9 | 5.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACEtapaProceso> |
| `sispro_sac_mecanismo_calculo` | `sispro_aspx` | 2 | 1.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACMecanismoCalculo> |
| `sispro_sac_origen_cobro` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACOrigenCobro> |
| `sispro_sac_tipo_cobro` | `sispro_aspx` | 2 | 1.7 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACTipoCobro> |
| `sispro_sac_tipo_servicio` | `sispro_aspx` | 4 | 2.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACTipoServicio> |
| `sispro_seg_materna_tipo_caso` | `sispro_aspx` | 13 | 8.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SegMaternaTipoCaso> |
| `sispro_ser_acto_admin_ejec` | `sispro_aspx` | 7 | 4.6 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SERActoAdminEjec> |
| `sispro_ser_acto_admin_incorp` | `sispro_aspx` | 5 | 3.5 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SERActoAdminIncorp> |
| `sispro_serid_recurso` | `sispro_aspx` | 14,000 | 9.7 MB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SERIDRecurso> |
| `sispro_si_no_pensionado` | `sispro_aspx` | 3 | 2.3 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SiNoPensionado> |
| `sispro_suf_comodin1` | `sispro_aspx` | 1 | 1.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SUFComodin1> |
| `sispro_suf_insumos_lentes_monturas_sten` | `sispro_aspx` | 19 | 12.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SUFInsumosLentesMonturasSten> |
| `sispro_tv_tipo_receptor` | `sispro_aspx` | 13 | 8.8 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TVTipoReceptor> |
| `sispro_tv_tipo_transferencia` | `sispro_aspx` | 11 | 7.9 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TVTipoTransferencia> |
| `sispro_umm` | `sispro_aspx` | 273 | 166.1 KB | <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=UMM> |

---

## Institucional (REPS, EAPB, IPS, redes)

### `eapb_codigos`  ·  1,717 filas  ·  1.3 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CodigoEAPByNit>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:53:13Z  ·  sha256 `cf30ddd2fa17…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:TipoRegimen`, `Extra_II:TipoID`, `Extra_III:NroID`, `Extra_IV:TipoEAPB`
  `Extra_V:Poblacion`, `Extra_VI:Email`, `Extra_VII:Orden`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CodigoEAPByNit`
  - `Codigo`: `05000`
  - `Nombre`: `DIRECCION DEPARTAMENTAL DE ANTIOQUIA`
  - `Descripcion`: `SECRETARIA SECCIONAL DE SALUD Y  PROTECCION SOCIAL DE ANTIOQUIA`
  - `Habilitado`: `SI`

### `ips_listado_nivel`  ·  11,466 filas  ·  8.9 MB

- **Kind**: `socrata`
- **URL**: <https://www.datos.gov.co/resource/ugc5-acjp.json>
- **Licencia**: Datos Abiertos Colombia (Ley 1712/2014)
- **Versión / sync**: 2022-06-17T14:45:35+00:00  ·  sha256 `3635d0e8cea1…`
- **Columnas** (24):
  `depa_nombre`, `muni_nombre`, `codigo_habilitacion`, `nombre_prestador`, `nits_nit`, `razon_social`
  `clpr_codigo`, `clpr_nombre`, `ese`, `direccion`, `telefono`, `fax`
  `email`, `nivel`, `caracter`, `habilitado`, `fecha_radicacion`, `fecha_vencimiento`
  `dv`, `clase_persona`, `naju_codigo`, `naju_nombre`, `numero_sede_principal`, `fecha_corte_reps`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `depa_nombre`: `Amazonas`
  - `muni_nombre`: `LETICIA`
  - `codigo_habilitacion`: `9100100019`
  - `nombre_prestador`: `E.S.E. HOSPITAL SAN RAFAEL DE LETICIA`
  - `nits_nit`: `838000096`

### `ips_por_nivel`  ·  41,427 filas  ·  35.3 MB

- **Kind**: `socrata`
- **URL**: <https://www.datos.gov.co/resource/s2ru-bqt6.json>
- **Licencia**: Datos Abiertos Colombia (Ley 1712/2014)
- **Versión / sync**: 2022-11-21T22:37:08+00:00  ·  sha256 `ca08fe3895ad…`
- **Columnas** (20):
  `departamento`, `municipio`, `c_digo_prestador`, `nombre_prestador`, `nit_ips`, `num_digito_verificion`
  `naturaleza`, `num_nivel_atencion`, `c_digo_sede`, `n_mero_sede`, `nom_sede_ips`, `gerente`
  `direcci_n`, `email`, `tel_fono`, `nom_grupo_capacidad`, `nom_descripcion_capacidad`, `num_cantidad_capacidad_instalada`
  `fecha_corte`, `fuente`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `departamento`: `Amazonas`
  - `municipio`: `EL ENCANTO`
  - `c_digo_prestador`: `9100100019`
  - `nombre_prestador`: `E.S.E. HOSPITAL SAN RAFAEL DE LETICIA`
  - `nit_ips`: `838000096`

### `reps_capacidades`  ·  97,136 filas  ·  102.0 MB

- **Kind**: `reps_export`
- **URL**: <https://prestadores.minsalud.gov.co/habilitacion/consultas/capacidadesinstaladas_reps.aspx>
- **Licencia**: MinSalud REPS — Registro Especial de Prestadores (consulta pública)
- **Versión / sync**: 2026-05-02T20:25:44Z  ·  sha256 `cd1421b80d0d…`
- **Notas**: Portal público prestadores.minsalud.gov.co/habilitacion (login guest invitado/invitado por diseño). Sin restricción en robots.txt. Cada sync descarga el export CSV completo via el botón oficial 'Exportar a Texto'.
- **Columnas** (31):
  `depa_nombre`, `muni_nombre`, `habi_codigo_habilitacion`, `nombre_prestador`, `codigo_habilitacion`, `numero_sede`
  `sede_nombre`, `nits_nit`, `dv`, `clase_persona`, `naju_codigo`, `naju_nombre`
  `clpr_codigo`, `clpr_nombre`, `ese`, `nivel`, `caracter`, `habilitado`
  `grupo_capacidad`, `coca_codigo`, `coca_nombre`, `cantidad`, `numero_sede_principal`, `numero_placa`
  `modalidad`, `modelo`, `numero_tarjeta`, `fecha_corte_REPS`, `direccion`, `email`
  `telefono`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `depa_nombre`: `Amazonas`
  - `muni_nombre`: `EL ENCANTO`
  - `habi_codigo_habilitacion`: `9100100019`
  - `nombre_prestador`: `E.S.E. HOSPITAL SAN RAFAEL DE LETICIA`
  - `codigo_habilitacion`: `9126300019`

### `reps_habilitados`  ·  60,828 filas  ·  72.8 MB

- **Kind**: `reps_export`
- **URL**: <https://prestadores.minsalud.gov.co/habilitacion/consultas/habilitados_reps.aspx>
- **Licencia**: MinSalud REPS — Registro Especial de Prestadores (consulta pública)
- **Versión / sync**: 2026-05-02T20:22:18Z  ·  sha256 `512ef276ae15…`
- **Notas**: Portal público prestadores.minsalud.gov.co/habilitacion (login guest invitado/invitado por diseño). Sin restricción en robots.txt. Cada sync descarga el export CSV completo via el botón oficial 'Exportar a Texto'.
- **Columnas** (36):
  `depa_nombre`, `muni_nombre`, `codigo_habilitacion`, `nombre_prestador`, `tido_codigo`, `nits_nit`
  `razon_social`, `clpr_codigo`, `clpr_nombre`, `ese`, `direccion`, `telefono`
  `fax`, `email`, `gerente`, `nivel`, `caracter`, `habilitado`
  `fecha_radicacion`, `fecha_vencimiento`, `fecha_cierre`, `dv`, `clase_persona`, `naju_codigo`
  `naju_nombre`, `numero_sede_principal`, `fecha_corte_REPS`, `telefono_adicional`, `email_adicional`, `rep_legal`
  `Municipio PDET`, `Municipio ZOMAC`, `Municipio PNIS`, `Municipio PNSR antes 2023`, `Municipio PNSR 2023`, `Municipio PNSR 2024`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `depa_nombre`: `Amazonas`
  - `muni_nombre`: `LETICIA`
  - `codigo_habilitacion`: `9100100148`
  - `nombre_prestador`: `ALEXANDER ABEL PEREZ FABRA`
  - `tido_codigo`: ``

### `reps_medidas_seguridad`  ·  3,443 filas  ·  4.8 MB

- **Kind**: `reps_export`
- **URL**: <https://prestadores.minsalud.gov.co/habilitacion/consultas/medidasseguridad_reps.aspx>
- **Licencia**: MinSalud REPS — Registro Especial de Prestadores (consulta pública)
- **Versión / sync**: 2026-05-02T20:32:57Z  ·  sha256 `84d983808a67…`
- **Notas**: Portal público prestadores.minsalud.gov.co/habilitacion (login guest invitado/invitado por diseño). Sin restricción en robots.txt. Cada sync descarga el export CSV completo via el botón oficial 'Exportar a Texto'.
- **Columnas** (40):
  `depa_nombre`, `muni_nombre`, `habi_codigo_habilitacion`, `codigo_habilitacion`, `numero_sede`, `sede_nombre`
  `direccion`, `telefono`, `email`, `nits_nit`, `dv`, `clase_persona`
  `naju_codigo`, `naju_nombre`, `clpr_codigo`, `clpr_nombre`, `ese`, `nivel`
  `caracter`, `grse_codigo`, `grse_nombre`, `serv_codigo`, `serv_nombre`, `ambulatorio`
  `hospitalario`, `unidad_movil`, `domiciliario`, `otras_extramural`, `centro_referencia`, `institucion_remisora`
  `complejidad_baja`, `complejidad_media`, `complejidad_alta`, `fecha_apertura`, `fecha_cierre`, `numero_distintivo`
  `numero_sede_principal`, `medidas_de_seguridad`, `fecha_corte_REPS`, `nombre_prestador`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `depa_nombre`: `Antioquia`
  - `muni_nombre`: `MEDELLÍN`
  - `habi_codigo_habilitacion`: `0500101997`
  - `codigo_habilitacion`: `0500101997`
  - `numero_sede`: `01`

### `reps_prestadores`  ·  76,821 filas  ·  74.2 MB

- **Kind**: `socrata`
- **URL**: <https://www.datos.gov.co/resource/c36g-9fc2.json>
- **Licencia**: Datos Abiertos Colombia (Ley 1712/2014)
- **Versión / sync**: 2026-04-17T19:57:23+00:00  ·  sha256 `44d810e45302…`
- **Columnas** (22):
  `codigoprestador`, `nombreprestador`, `codigohabilitacionsede`, `nombresede`, `tipoid`, `numeroidentificacion`
  `naturalezajuridica`, `ese`, `municipio_prestador`, `departamentoprestadordesc`, `municipioprestadordesc`, `direccionprestador`
  `email_prestador`, `telefonoprestador`, `municipiosede`, `departamentodededesc`, `municipiosededesc`, `direcci_nsede`
  `email_sede`, `t_lefonosede`, `claseprestador`, `fecha_corte_reps`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `codigoprestador`: `9100100017`
  - `nombreprestador`: `MANUEL DE JESUS LUBO OROZCO`
  - `codigohabilitacionsede`: `910010001701`
  - `nombresede`: `MANUEL DE JESUS LUBO OROZCO`
  - `tipoid`: `CC`

### `reps_sanciones`  ·  788 filas  ·  1.1 MB

- **Kind**: `reps_export`
- **URL**: <https://prestadores.minsalud.gov.co/habilitacion/consultas/sanciones_reps.aspx>
- **Licencia**: MinSalud REPS — Registro Especial de Prestadores (consulta pública)
- **Versión / sync**: 2026-05-02T20:33:06Z  ·  sha256 `5a10954c9a13…`
- **Notas**: Portal público prestadores.minsalud.gov.co/habilitacion (login guest invitado/invitado por diseño). Sin restricción en robots.txt. Cada sync descarga el export CSV completo via el botón oficial 'Exportar a Texto'.
- **Columnas** (41):
  `depa_nombre`, `muni_nombre`, `habi_codigo_habilitacion`, `codigo_habilitacion`, `numero_sede`, `sede_nombre`
  `direccion`, `telefono`, `email`, `nits_nit`, `dv`, `clase_persona`
  `naju_codigo`, `naju_nombre`, `clpr_codigo`, `clpr_nombre`, `ese`, `nivel`
  `caracter`, `grse_codigo`, `grse_nombre`, `serv_codigo`, `serv_nombre`, `ambulatorio`
  `hospitalario`, `unidad_movil`, `domiciliario`, `otras_extramural`, `centro_referencia`, `institucion_remisora`
  `complejidad_baja`, `complejidad_media`, `complejidad_alta`, `fecha_apertura`, `fecha_cierre`, `numero_distintivo`
  `numero_sede_principal`, `sanciones`, `fecha_corte_REPS`, `nombre_prestador`, `medidas_de_seguridad`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `depa_nombre`: `Antioquia`
  - `muni_nombre`: `MEDELLÍN`
  - `habi_codigo_habilitacion`: `0500102178`
  - `codigo_habilitacion`: `0500102178`
  - `numero_sede`: `61`

### `reps_sedes`  ·  76,561 filas  ·  117.4 MB

- **Kind**: `reps_export`
- **URL**: <https://prestadores.minsalud.gov.co/habilitacion/consultas/sedes_reps.aspx>
- **Licencia**: MinSalud REPS — Registro Especial de Prestadores (consulta pública)
- **Versión / sync**: 2026-05-02T20:22:35Z  ·  sha256 `ef9e2ced00ff…`
- **Notas**: Portal público prestadores.minsalud.gov.co/habilitacion (login guest invitado/invitado por diseño). Sin restricción en robots.txt. Cada sync descarga el export CSV completo via el botón oficial 'Exportar a Texto'.
- **Columnas** (47):
  `departamento`, `municipio`, `codigo_prestador`, `nombre_prestador`, `codigo_habilitacion`, `numero_sede`
  `nombre`, `gerente`, `tipo_zona`, `direccion`, `barrio`, `cepo_codigo`
  `centro_poblado`, `telefono`, `fax`, `email`, `fecha_apertura`, `fecha_cierre`
  `nits_nit`, `dv`, `clase_persona`, `naju_codigo`, `naturaleza`, `clpr_codigo`
  `clase_prestador`, `ese`, `nivel`, `caracter`, `sede_principal`, `habilitado`
  `numero_sede_principal`, `horario_lunes`, `horario_martes`, `horario_miercoles`, `horario_jueves`, `horario_viernes`
  `horario_sabado`, `horario_domingo`, `fecha_corte_REPS`, `telefono_adicional`, `email_adicional`, `Municipio PDET`
  `Municipio ZOMAC`, `Municipio PNIS`, `Municipio PNSR antes 2023`, `Municipio PNSR 2023`, `Municipio PNSR 2024`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `departamento`: `Amazonas`
  - `municipio`: `EL ENCANTO`
  - `codigo_prestador`: `9100100019`
  - `nombre_prestador`: `E.S.E. HOSPITAL SAN RAFAEL DE LETICIA`
  - `codigo_habilitacion`: `9126300019`

### `reps_servicios`  ·  228,293 filas  ·  854.9 MB

- **Kind**: `reps_export`
- **URL**: <https://prestadores.minsalud.gov.co/habilitacion/consultas/serviciossedes_reps.aspx>
- **Licencia**: MinSalud REPS — Registro Especial de Prestadores (consulta pública)
- **Versión / sync**: 2026-05-02T20:25:12Z  ·  sha256 `49ad7f46b2d3…`
- **Notas**: Portal público prestadores.minsalud.gov.co/habilitacion (login guest invitado/invitado por diseño). Sin restricción en robots.txt. Cada sync descarga el export CSV completo via el botón oficial 'Exportar a Texto'. Volumen alto — el export tarda ~95s.
- **Columnas** (94):
  `depa_nombre`, `muni_nombre`, `habi_codigo_habilitacion`, `codigo_habilitacion`, `numero_sede`, `sede_nombre`
  `direccion`, `telefono`, `email`, `nits_nit`, `dv`, `clase_persona`
  `naju_codigo`, `naju_nombre`, `clpr_codigo`, `clpr_nombre`, `ese`, `nivel`
  `caracter`, `habilitado`, `grse_codigo`, `grse_nombre`, `serv_codigo`, `serv_nombre`
  `ambulatorio`, `hospitalario`, `unidad_movil`, `domiciliario`, `otras_extramural`, `centro_referencia`
  `institucion_remisora`, `complejidad_baja`, `complejidad_media`, `complejidad_alta`, `fecha_apertura`, `fecha_cierre`
  `numero_distintivo`, `numero_sede_principal`, `observaciones_serv_Res3100_2019`, `fecha_corte_REPS`, `nombre`, `horario_lunes`
  `horario_martes`, `horario_miercoles`, `horario_jueves`, `horario_viernes`, `horario_sabado`, `horario_domingo`
  `modalidad_intramural`, `Modalidad Extramural Transporte Asistencial y APH`, `Modalidad Extramural Unidad Móvil`, `Modalidad Extramural Domiciliaria`, `Modalidad Extramural Jornadas de Salud`, `modalidad_telemedicina`
  `modalidad_prestador_referencia`, `modalidad_prestador_referencia_telemedicina_interactiva`, `modalidad_prestador_referencia_telemedicina_no_interactiva`, `modalidad_prestador_referencia_tele_experticia`, `modalidad_prestador_referencia_tele_monitoreo`, `modalidad_prestador_remisor`
  `modalidad_prestador_remisor_tele_experticia`, `modalidad_prestador_remisor_tele_monitoreo`, `complejidades`, `especificidad_oncologico`, `especificidad_trasplante_osteomuscular`, `especificidad_trasplante_piel`
  `especificidad_trasplante_cardiovascular`, `especificidad_trasplante_tejido_ocular`, `especificidad_atencion_paciente_quemado`, `especificidad_salud_mental`, `especificidad_spa`, `especificidad_otras_patologias`
  `especificidad_trasplante_celulas_progenitoras_hematopoyeticas`, `especificidad_procedimientos_quirurgicos_ambulatorios`, `especificidad_organo_rinon`, `especificidad_organo_higado`, `especificidad_organo_pancreas`, `especificidad_organo_intestino`
  `especificidad_organo_multivisceral`, `especificidad_organo_corazon`, `especificidad_organo_pulmon`, `especificidad_sustancias_psicoactivas`, `especificidad_trasplante_renal`, `version_norma`
  `email_adicional`, `telefono_adicional`, `gerente`, `Municipio PDET`, `Municipio ZOMAC`, `Municipio PNIS`
  `Municipio PNSR antes 2023`, `Municipio PNSR 2023`, `Municipio PNSR 2024`, `razon_social`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `depa_nombre`: `Antioquia`
  - `muni_nombre`: `MEDELLÍN`
  - `habi_codigo_habilitacion`: `0500100003`
  - `codigo_habilitacion`: `0500100003`
  - `numero_sede`: `01`

### `servicios_habilitados`  ·  1,859 filas  ·  1.4 MB

- **Kind**: `socrata`
- **URL**: <https://www.datos.gov.co/resource/p9n2-9qsb.json>
- **Licencia**: Datos Abiertos Colombia (Ley 1712/2014)
- **Versión / sync**: 2023-06-28T20:28:27+00:00  ·  sha256 `0949d4b0c169…`
- **Columnas** (21):
  `municipio`, `codigo_habilitacion`, `num_sede`, `nombre_sede_prestador`, `grse_codigo`, `grse_nombre`
  `codigo_servicio`, `servicio`, `ambulatorio`, `hospitalario`, `unidad_movil`, `domiciliario`
  `otras_extramural`, `centro_referencia`, `institucion_remisora`, `complejidad_baja`, `complejidad_media`, `complejidad_alta`
  `fecha_apertura`, `numero_distintivo`, `complejidades`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `municipio`: `TUNJA`
  - `codigo_habilitacion`: `1500100266`
  - `num_sede`: `1`
  - `nombre_sede_prestador`: `EMPRESA SOCIAL DEL ESTADO CENTRO DE REHABILITACION INTEGRAL DE BOYACA`
  - `grse_codigo`: `7`

### `sispro_cod_eapbrnse`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CodEAPBRNSE>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:05Z  ·  sha256 `a1bfd1b48e5c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:TipoRegimen`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CodEAPBRNSE`
  - `Codigo`: `EPS008`
  - `Nombre`: `Compensar EPS`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cod_sede_ips_demo`  ·  223 filas  ·  141.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CodSedeIPSDemo>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:06Z  ·  sha256 `7289a9bc3d2f…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CodSedeIPSDemo`
  - `Codigo`: `050010239301`
  - `Nombre`: `ESE HOSPITAL  CARISMA`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cpti_peligros_condicionesde_seguridad`  ·  12 filas  ·  8.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIPeligrosCondicionesdeSeguridad>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:07Z  ·  sha256 `73b24814e290…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CPTIPeligrosCondicionesdeSeguridad`
  - `Codigo`: `1`
  - `Nombre`: `Uso de herramientas manaules, herramientas cortopunzantes, maquinaria, equipos`
  - `Descripcion`: `CPTI Peligro por Condiciones de seguridad`
  - `Habilitado`: `SI`

### `sispro_entidades_pma140_gipm`  ·  1,274 filas  ·  777.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EntidadesPMA140GIPM>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:08Z  ·  sha256 `ddd93378a7ce…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EntidadesPMA140GIPM`
  - `Codigo`: `800000118`
  - `Nombre`: `EMPRESA SOCIAL DEL ESTADO HOSPITAL UNIVERSITARIO SAN JUAN DE DIOS`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_entidades_pts`  ·  280 filas  ·  233.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EntidadesPTS>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:08Z  ·  sha256 `6637c91ff354…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:TipoIDEntidad`, `Extra_II:NumeroIDEntidad`, `Extra_III:DV`, `Extra_IV:FechaCreacion`
  `Extra_V:FechaInicioOperacion`, `Extra_VI:TiposEntidad`, `Extra_VII:CodigoDepartamento`, `Extra_VIII:CodigoMunicipio`, `Extra_IX:Direccion`, `Extra_X:EmailEntidad`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EntidadesPTS`
  - `Codigo`: `NI1014203459`
  - `Nombre`: `LEIDY CUESTAS`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_fne_subtipo_entidad`  ·  28 filas  ·  17.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNESubtipoEntidad>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:09Z  ·  sha256 `ed9d5c0aff50…`
- **Columnas** (21):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Aplicación`, `Extra_II:Tipo Entidad`, `Extra_IV`, `Extra_V`
  `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`, `ValorRegistro`
  `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FNESubtipoEntidad`
  - `Codigo`: `1`
  - `Nombre`: `ARL`
  - `Descripcion`: `Administradora de riesgos laborales`
  - `Habilitado`: `SI`

### `sispro_ind_uso_entidad_en_sac`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IndUsoEntidadEnSAC>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:10Z  ·  sha256 `24102ecfdb2a…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IndUsoEntidadEnSAC`
  - `Codigo`: `INV`
  - `Nombre`: `INV Indicador de entidad invalida para Giro de SAC`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_ips_sub_red`  ·  24 filas  ·  15.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IPSSubRed>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:10Z  ·  sha256 `15f0a9643e7c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:NitSubRed`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IPSSubRed`
  - `Codigo`: `800196433`
  - `Nombre`: `HOSPITAL SIMON BOLIVAR E.S.E.`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_lce_entidades_poblacion_elegible_subsidia_salud2_na`  ·  9 filas  ·  7.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LCEEntidadesPoblacionElegibleSubsidiaSalud2NA>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:11Z  ·  sha256 `71f0095b7ce7…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `LCEEntidadesPoblacionElegibleSubsidiaSalud2NA`
  - `Codigo`: `800152783`
  - `Nombre`: `Fiscalía General de la Nación`
  - `Descripcion`: `LCE Entidades Población Elegible Subsidia Salud Valor 2 NA`
  - `Habilitado`: `SI`

### `sispro_rmips_no_reps`  ·  1 filas  ·  1.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RMIPSNoREPS>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:11Z  ·  sha256 `500fd691fbf5…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RMIPSNoREPS`
  - `Codigo`: `800150861`
  - `Nombre`: `Instituto Nacional de Medicina Legal y Ciencias Forenses`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_rua_codigo_entidad_supervivencia`  ·  456 filas  ·  307.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RUACodigoEntidadSupervivencia>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:12Z  ·  sha256 `c48f0eadbe5d…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:TipoID`, `Extra_II:NroID`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RUACodigoEntidadSupervivencia`
  - `Codigo`: `14-17`
  - `Nombre`: `SEGUROS DE VIDA ALFA S A`
  - `Descripcion`: `SEGUROS DE VIDA ALFA S A`
  - `Habilitado`: `SI`

### `sispro_sac_tipo_entidad`  ·  4 filas  ·  2.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACTipoEntidad>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:12Z  ·  sha256 `37c064ec1c3d…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SACTipoEntidad`
  - `Codigo`: `EPS`
  - `Nombre`: `EPS`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_sacip_sy_eps_svalidasx_fepa`  ·  22 filas  ·  14.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACIPSyEPSSvalidasxFEPA>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:13Z  ·  sha256 `c6fad4ff48e0…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SACIPSyEPSSvalidasxFEPA`
  - `Codigo`: `804002105`
  - `Nombre`: `Comparta - Cooperativa de Salud Comunitaria Comparta EPS S`
  - `Descripcion`: ``
  - `Habilitado`: `SI`


## Clínico (diagnósticos, procedimientos, medicamentos, vacunas, enfermedades)

### `cie10`  ·  14,000 filas  ·  10.8 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CIE10>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:53:24Z  ·  sha256 `aaa212ee72d0…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:AplicaASexo`, `Extra_II:EdadMinima`, `Extra_III:EdadMaxima`, `Extra_IV:GrupoMortalidad`
  `Extra_V`, `Extra_VI:Capitulo`, `Extra_VII:Grupo`, `Extra_VIII:SubGrupo`, `Extra_IX:Categoria`, `Extra_X:Sexo`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CIE10`
  - `Codigo`: `A000`
  - `Nombre`: `COLERA DEBIDO A VIBRIO CHOLERAE 01, BIOTIPO CHOLERAE`
  - `Descripcion`: `COLERA`
  - `Habilitado`: `SI`

### `cups`  ·  12,000 filas  ·  9.6 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CUPS>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:53:33Z  ·  sha256 `2a2578ef3bb6…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Cobertura`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CUPS`
  - `Codigo`: `010101`
  - `Nombre`: `PUNCIÓN CISTERNAL- VÍA LATERAL`
  - `Descripcion`: `CapItulo 01 SISTEMA NERVIOSO`
  - `Habilitado`: `SI`

### `glosario_medico`  ·  900 filas  ·  502.8 KB

- **Kind**: `socrata`
- **URL**: <https://www.datos.gov.co/resource/98ms-bv6s.json>
- **Licencia**: Datos Abiertos Colombia (Ley 1712/2014)
- **Versión / sync**: 2023-07-27T22:27:54+00:00  ·  sha256 `8f83a7ce07fc…`
- **Columnas** (5):
  `palabra`, `descripcion`, `rankingbusqueda`, `palabra_min`, `descripcion_min`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `palabra`: `ABLACIÓN`
  - `descripcion`: `Procedimiento quirúrgico mediante el cual se extraen por separación o extirpa…`
  - `rankingbusqueda`: `30`
  - `palabra_min`: `ablación`
  - `descripcion_min`: `procedimiento quirúrgico mediante el cual se extraen por separación o extirpa…`

### `ium_medicamentos`  ·  36,000 filas  ·  33.4 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IUM>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:53:59Z  ·  sha256 `1a51b1c13cac…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:IUMNivel_I`, `Extra_II:PrincipioActivo`, `Extra_III:CodigoPrincipioActivo`, `Extra_IV:FormaFarmaceutica`
  `Extra_V:CodigoFormaFarmaceutica`, `Extra_VI:IUMNivel_II`, `Extra_VII:CodigoFormaComercializacion`, `Extra_VIII:IUMNivel_III`, `Extra_IX:CondicionRegistroMuestraMedica`, `Extra_X:UnidadEmpaque`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IUM`
  - `Codigo`: `0`
  - `Nombre`: `0`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `medicamentos_pbs`  ·  2,067 filas  ·  1.6 MB

- **Kind**: `socrata`
- **URL**: <https://www.datos.gov.co/resource/jtqe-tuvf.json>
- **Licencia**: Datos Abiertos Colombia (Ley 1712/2014)
- **Versión / sync**: 2023-07-27T23:26:40+00:00  ·  sha256 `7276b8e1cd49…`
- **Columnas** (12):
  `id`, `codigoatc`, `principioactivo`, `rankingbusqueda`, `resumen`, `formafarmaceutica`
  `aclaracion`, `item`, `principioactivo_min`, `formafarmaceutica_min`, `coberturaplanbeneficiosupc`, `coberturaplanbeneficiosupc_min`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `id`: `10244`
  - `codigoatc`: `J05AF06`
  - `principioactivo`: `ABACAVIR`
  - `rankingbusqueda`: `1660`
  - `resumen`: `Incluye todas las concentraciones y formas farmacéuticas`

### `procedimientos_pbs`  ·  8,114 filas  ·  9.8 MB

- **Kind**: `socrata`
- **URL**: <https://www.datos.gov.co/resource/9zcz-bjue.json>
- **Licencia**: Datos Abiertos Colombia (Ley 1712/2014)
- **Versión / sync**: 2023-07-27T23:18:45+00:00  ·  sha256 `db25decb2044…`
- **Columnas** (17):
  `codigoprocedimiento`, `codigocups`, `descripcion`, `quees`, `coberturaplanbeneficiosupc`, `detalleplanbeneficiosupc`
  `codigozonaanatomica`, `rankingbusqueda`, `codigoanatomicanivelii`, `codigoanatomicaniveli`, `descripcion_min`, `quees_min`
  `coberturaplanbeneficiosupc_min`, `detalleplanbeneficiosupc_min`, `codigocuerpo3d`, `codigoareatopografica`, `nombrecuerpo3d`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `codigoprocedimiento`: `57465`
  - `codigocups`: `10101`
  - `descripcion`: `PUNCIÓN CISTERNAL VÍA LATERAL`
  - `quees`: `Procedimiento para extraer evaluar y medir la presión del líquido cefalorraqu…`
  - `coberturaplanbeneficiosupc`: `Financiado con recursos de la Unidad de Pago por Capitación (UPC)`

### `sispro_aco_tipo_soporte_documental`  ·  6 filas  ·  4.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOTipoSoporteDocumental>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:24Z  ·  sha256 `eaea79a6bafe…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ACOTipoSoporteDocumental`
  - `Codigo`: `01`
  - `Nombre`: `Certificación Financiera donde conste la existencia de los recursos o certifi…`
  - `Descripcion`: `Tipo de documento al cual corresponde el soporte digitalizado`
  - `Habilitado`: `SI`

### `sispro_aps_acceso_vivienda`  ·  5 filas  ·  3.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSAccesoVivienda>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:25Z  ·  sha256 `a7ca88cb7828…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `APSAccesoVivienda`
  - `Codigo`: `1`
  - `Nombre`: `Medios de transporte (Buses, autos, camiones, lanchas, etc)`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_aps_accion_intersectorial`  ·  9 filas  ·  6.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSAccionIntersectorial>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:25Z  ·  sha256 `0073aa9cd575…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `APSAccionIntersectorial`
  - `Codigo`: `IS01001`
  - `Nombre`: `Vivienda-mejoramiento de pisos y paredes`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_aps_agente_medicina`  ·  4 filas  ·  2.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSAgenteMedicina>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:26Z  ·  sha256 `5e730ddcde4b…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `APSAgenteMedicina`
  - `Codigo`: `1`
  - `Nombre`: `Médico tradicional`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_aps_animales`  ·  13 filas  ·  8.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSAnimales>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:26Z  ·  sha256 `3d98f6684eae…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `APSAnimales`
  - `Codigo`: `1`
  - `Nombre`: `Perros`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_aps_diagnostico_nutricion`  ·  7 filas  ·  4.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSDiagnosticoNutricion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:27Z  ·  sha256 `466731503f69…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `APSDiagnosticoNutricion`
  - `Codigo`: `1`
  - `Nombre`: `Obesidad`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_aps_disposicion_residuos`  ·  6 filas  ·  4.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSDisposicionResiduos>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:28Z  ·  sha256 `242fecb1b92e…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `APSDisposicionResiduos`
  - `Codigo`: `1`
  - `Nombre`: `Recolección por parte del servicio de aseo distrital o municipal`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_aps_ecomapa`  ·  5 filas  ·  3.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSEcomapa>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:28Z  ·  sha256 `16cbe4372296…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `APSEcomapa`
  - `Codigo`: `1`
  - `Nombre`: `Positivo`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_aps_enfermedad_transmisible`  ·  8 filas  ·  5.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSEnfermedadTransmisible>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:29Z  ·  sha256 `4664aad79cc7…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `APSEnfermedadTransmisible`
  - `Codigo`: `1`
  - `Nombre`: `TB`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_aps_excreta`  ·  8 filas  ·  5.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSExcreta>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:29Z  ·  sha256 `6596f20ae5a6…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `APSExcreta`
  - `Codigo`: `1`
  - `Nombre`: `Sanitario conectado al alcantarillado`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_apsapgar`  ·  4 filas  ·  2.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=APSAPGAR>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:30Z  ·  sha256 `d1cf3359b600…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `APSAPGAR`
  - `Codigo`: `1`
  - `Nombre`: `Normal`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_area_covid`  ·  2 filas  ·  1.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=AreaCovid>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:30Z  ·  sha256 `a41418d376cc…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `AreaCovid`
  - `Codigo`: `01`
  - `Nombre`: `Área COVID`
  - `Descripcion`: `Área COVID`
  - `Habilitado`: `SI`

### `sispro_catalogo_cu_ms`  ·  164,000 filas  ·  149.9 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CatalogoCUMs>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:56:28Z  ·  sha256 `6b88b01429ac…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:IndicadorMuestraMedica`, `Extra_II:Cod_ATC`, `Extra_III:ATC`, `Extra_IV:RegistroSanitario`
  `Extra_V:PrincipioActivo`, `Extra_VI:CantidadPrincipioActivo`, `Extra_VII:UnidadMedidaPrincipioActivo`, `Extra_VIII:ViaAdministracion`, `Extra_IX:CantidadPresentacion`, `Extra_X:UnidadMedidaPresentacion`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CatalogoCUMs`
  - `Codigo`: `10042-1`
  - `Nombre`: `FLUNARICINA 10 MG`
  - `Descripcion`: `CAJA X 2 BLISTER X 10 TABLETAS BLISTER ALUMINIO - PVC`
  - `Habilitado`: `SI`

### `sispro_categoria_medicamento`  ·  7 filas  ·  4.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CategoriaMedicamento>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:56:30Z  ·  sha256 `368cf72546b9…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CategoriaMedicamento`
  - `Codigo`: `1`
  - `Nombre`: `BIOLOGICO`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_clasificacion_atc`  ·  6,000 filas  ·  3.6 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ClasificacionATC>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:56:35Z  ·  sha256 `d883db67683d…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Nivel`, `Extra_II:NivelSuperior`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ClasificacionATC`
  - `Codigo`: `A`
  - `Nombre`: `TRACTO ALIMENTARIO Y METABOLISMO`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cups04y05`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CUPS04y05>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:56:35Z  ·  sha256 `3520ee3ea188…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CUPS04y05`
  - `Codigo`: `04`
  - `Nombre`: `Detección de Alteraciones de Crecimiento y Desarrollo`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cups_anterior`  ·  12,000 filas  ·  8.6 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CUPSAnterior>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:56:43Z  ·  sha256 `2b7a83e8f9e4…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV:Sexo`
  `Extra_V:Ambito`, `Extra_VI:Estancia`, `Extra_VII:Cobertura`, `Extra_VIII:Duplicado`, `Extra_IX:Vida`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CUPSAnterior`
  - `Codigo`: `010101`
  - `Nombre`: `PUNCION CISTERNAL, VIA LATERAL`
  - `Descripcion`: `Capitulo 01 SISTEMA NERVIOSO`
  - `Habilitado`: `SI`

### `sispro_cups_gr_servicios`  ·  1,444,000 filas  ·  855.0 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CUPSGrServicios>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:13:34Z  ·  sha256 `6f83765ed761…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:CUPS`, `Extra_II:GrServicios`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CUPSGrServicios`
  - `Codigo`: `1`
  - `Nombre`: `DCX1`
  - `Descripcion`: `DCX1`
  - `Habilitado`: `SI`

### `sispro_cups_rips`  ·  14,000 filas  ·  10.2 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CUPSRips>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:13:49Z  ·  sha256 `23cca0892bc2…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:UsoCodigoCUP`, `Extra_II:Qx`, `Extra_III:NroMinimo`, `Extra_IV:NroMaximo`
  `Extra_V:DxRequerido`, `Extra_VI:Sexo`, `Extra_VII:Ambito`, `Extra_VIII:Estancia`, `Extra_IX:Cobertura`, `Extra_X:Duplicado`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CUPSRips`
  - `Codigo`: `010100`
  - `Nombre`: `PUNCION CISTERNAL SOD`
  - `Descripcion`: `SECCION 00 PROCEDIMIENTOS QUIRURGICOS`
  - `Habilitado`: `SI`

### `sispro_cupscie`  ·  1,581 filas  ·  1.2 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CUPSCIE>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:13:50Z  ·  sha256 `914fac73438d…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:SEXO`, `Extra_II:AMBITO`, `Extra_III:ESTANCIA`, `Extra_IV:COBERTURA`
  `Extra_V:DUPLICADO`, `Extra_VI:VIDA`, `Extra_VII:DX_RELACIONADO`, `Extra_VIII:TR_ANIO_INI_VIGENCIA`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CUPSCIE`
  - `Codigo`: `1`
  - `Nombre`: `RESECCION DE QUISTE O CONDUCTO TIROGLOSO VIA ABIERTA`
  - `Descripcion`: `RESECCION DE QUISTE O CONDUCTO TIROGLOSO VIA ABIERTA`
  - `Habilitado`: `SI`

### `sispro_dispositivos_medicos`  ·  21 filas  ·  15.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DispositivosMedicos>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:13:51Z  ·  sha256 `e627c022e2e1…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:VersionMIPRES`, `Extra_II:FechaMIPRES`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `DispositivosMedicos`
  - `Codigo`: `011`
  - `Nombre`: `BOLSA>104 AL AÑO; EN CANCER COLON O RECTO`
  - `Descripcion`: `BOLSA>104 AL AÑO; EN CANCER COLON O RECTO`
  - `Habilitado`: `NO`

### `sispro_dispositivos_medicos_libertad_vigilada`  ·  8,000 filas  ·  7.7 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DispositivosMedicosLibertadVigilada>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:13:57Z  ·  sha256 `1759d600c7dc…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Marca`, `Extra_II:Referencias`, `Extra_III:RegistroSanitario`, `Extra_IV:EstadoRegistro`
  `Extra_V:Titular`, `Extra_VI:Fabricante`, `Extra_VII:Importador`, `Extra_VIII:NivelRiesgo`, `Extra_IX:PresentacionComercial`, `Extra_X:UnidadUso`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `DispositivosMedicosLibertadVigilada`
  - `Codigo`: `19913478-1`
  - `Nombre`: `CONDONES TAHITI Y CONDONES HAWAII`
  - `Descripcion`: `ANTICONCEPTIVO DE BARRERA`
  - `Habilitado`: `SI`

### `sispro_dmes_categoria_reactivo`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESCategoriaReactivo>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:13:58Z  ·  sha256 `e696d972a331…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `DMESCategoriaReactivo`
  - `Codigo`: `1`
  - `Nombre`: `CATEGORIA I`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_dmes_presentacion_comercial`  ·  131 filas  ·  77.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESPresentacionComercial>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:13:58Z  ·  sha256 `ab4f5138f2bc…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `DMESPresentacionComercial`
  - `Codigo`: `1`
  - `Nombre`: `AMPOLLA`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_enfermedad_huerfana`  ·  4,000 filas  ·  2.6 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EnfermedadHuerfana>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:01Z  ·  sha256 `c88adb0f0a95…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:MIPRESVersionCreacion`, `Extra_II:MIPRESVersionActualizacion`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EnfermedadHuerfana`
  - `Codigo`: `1`
  - `Nombre`: `3MC Sindrome de Deficiencia COLEC11`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_entidad_financiera_nit`  ·  24 filas  ·  15.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EntidadFinancieraNit>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:01Z  ·  sha256 `fd70aff6b427…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:CodEntidadFinanciera`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EntidadFinancieraNit`
  - `Codigo`: `800037800`
  - `Nombre`: `banco agrario de colombia s.a.`
  - `Descripcion`: `banco agrario`
  - `Habilitado`: `SI`

### `sispro_estado_registro_sanitario`  ·  10 filas  ·  6.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EstadoRegistroSanitario>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:02Z  ·  sha256 `1f1848de5c81…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EstadoRegistroSanitario`
  - `Codigo`: `A`
  - `Nombre`: `ABANDONO`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_finalidad_cups`  ·  990 filas  ·  591.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FinalidadCUPS>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:03Z  ·  sha256 `1a0604ccb668…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Finalidad`, `Extra_II:CUPS`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FinalidadCUPS`
  - `Codigo`: `1`
  - `Nombre`: `ab1`
  - `Descripcion`: `ab1`
  - `Habilitado`: `SI`

### `sispro_forma_farmaceutica`  ·  61 filas  ·  36.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FormaFarmaceutica>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:04Z  ·  sha256 `849b88ba74a4…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FormaFarmaceutica`
  - `Codigo`: `AR`
  - `Nombre`: `AEROSOLES`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_medicamentos_dci`  ·  16,000 filas  ·  9.7 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=MedicamentosDCI>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:14Z  ·  sha256 `2a74be2b1a90…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `MedicamentosDCI`
  - `Codigo`: `1`
  - `Nombre`: `HIDRALAZINA`
  - `Descripcion`: `Medicamento`
  - `Habilitado`: `SI`

### `sispro_pagos_covid19_unilateral`  ·  231 filas  ·  181.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PagosCOVID19Unilateral>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:15Z  ·  sha256 `be690dae0790…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:NITPrestador`, `Extra_II:NomPrestador`, `Extra_III:CodSede`, `Extra_IV:NomSede`
  `Extra_V:FechaInicio`, `Extra_VI:FechaFin`, `Extra_VII:CodMpio`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PagosCOVID19Unilateral`
  - `Codigo`: `1`
  - `Nombre`: `ATENCION PREHOSPITLARIA Y SEGURIDAD INDUSTRIAL APREHSI LTDA`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_pai_mecanismo_vacuna`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PAIMecanismoVacuna>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:16Z  ·  sha256 `fc4198926f3c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PAIMecanismoVacuna`
  - `Codigo`: `1`
  - `Nombre`: `Vacunado EPS`
  - `Descripcion`: `Vacunado EPS`
  - `Habilitado`: `SI`

### `sispro_productos_nutricionales`  ·  314 filas  ·  222.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ProductosNutricionales>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:16Z  ·  sha256 `f438c341a08e…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:VersionMIPRES`, `Extra_II:FechaMIPRES`, `Extra_III:GrupoNivel1`, `Extra_IV:Forma`
  `Extra_V:PresentacionComercial`, `Extra_VI:Unidades`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ProductosNutricionales`
  - `Codigo`: `110201`
  - `Nombre`: `Ensure compact`
  - `Descripcion`: `Ensure compact`
  - `Habilitado`: `NO`

### `sispro_red_servicios_thscovid`  ·  226 filas  ·  142.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RedServiciosTHSCOVID>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:17Z  ·  sha256 `f73143883e48…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RedServiciosTHSCOVID`
  - `Codigo`: `101`
  - `Nombre`: `GENERAL ADULTOS`
  - `Descripcion`: `GENERAL ADULTOS`
  - `Habilitado`: `SI`

### `sispro_rlcpd_actividades_cuidado`  ·  19 filas  ·  13.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDActividadesCuidado>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:18Z  ·  sha256 `30bde033487d…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:NoAsisteServicioSalud`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RLCPDActividadesCuidado`
  - `Codigo`: `01`
  - `Nombre`: `Apoyo en actividades para el vestuario de la persona que requiere cuidado o a…`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_rlcpd_barreras_lugar`  ·  9 filas  ·  6.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDBarrerasLugar>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:18Z  ·  sha256 `2aa418bf2533…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:RLCPDBarrerasLugar`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RLCPDBarrerasLugar`
  - `Codigo`: `1`
  - `Nombre`: `Presencia de escaleras / falta de rampa`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_rlcpd_clase_adecuaciones`  ·  5 filas  ·  4.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDClaseAdecuaciones>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:19Z  ·  sha256 `889a75d31a34…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:RLCPDClaseAdecuaciones`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RLCPDClaseAdecuaciones`
  - `Codigo`: `1`
  - `Nombre`: `Accesibilidad al inmueble y a sus zonas comunes (ampliación de espacios, elim…`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_rlcpd_consecuencias_negativas`  ·  11 filas  ·  7.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDConsecuenciasNegativas>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:19Z  ·  sha256 `8f4a993eb837…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:RLCPDConsecuenciasNegativas`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RLCPDConsecuenciasNegativas`
  - `Codigo`: `01`
  - `Nombre`: `Sobrecarga en tareas domésticas`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_rlcpd_efectos_positivos`  ·  5 filas  ·  3.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDEfectosPositivos>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:20Z  ·  sha256 `25024ec3521c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:RLCPDEfectosPositivos`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RLCPDEfectosPositivos`
  - `Codigo`: `1`
  - `Nombre`: `Satisfacción por ayudar a otro`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_rlcpd_horas_autocuidado`  ·  3 filas  ·  2.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDHorasAutocuidado>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:20Z  ·  sha256 `24f53712876c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:RLCPDHorasAutocuidado`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RLCPDHorasAutocuidado`
  - `Codigo`: `1`
  - `Nombre`: `Menos una hora diaria`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_rlcpd_horas_cuidado`  ·  4 filas  ·  3.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RLCPDHorasCuidado>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:21Z  ·  sha256 `f444fde78dfb…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:RLCPDHorasCuidado`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RLCPDHorasCuidado`
  - `Codigo`: `1`
  - `Nombre`: `Entre 1 y 2 horas`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_ser_tipo_documento_soporte`  ·  16 filas  ·  11.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SERTipoDocumentoSoporte>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:21Z  ·  sha256 `c8c92b3928d1…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SERTipoDocumentoSoporte`
  - `Codigo`: `D01`
  - `Nombre`: `01.Incorporacion`
  - `Descripcion`: `ACTO ADMINISTRATIVO DE LA INCORPORACIÓN DE LOS RECURSOS A SU PRESUPUESTO`
  - `Habilitado`: `SI`

### `sispro_tipo_medicamento_pos`  ·  2 filas  ·  1.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoMedicamentoPOS>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:22Z  ·  sha256 `7bbcc0f7a182…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoMedicamentoPOS`
  - `Codigo`: `1`
  - `Nombre`: `Medicamento POS`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipo_producto_nutricional`  ·  22 filas  ·  16.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoProductoNutricional>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:22Z  ·  sha256 `9f3582a1157b…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:VersionMIPRES`, `Extra_II:FechaMIPRES`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoProductoNutricional`
  - `Codigo`: `1101`
  - `Nombre`: `Sustitutos de comidas intermedias - 75 a 150 kcal no deben sobrepasar las 120…`
  - `Descripcion`: `Sustitutos de comidas intermedias - 75 a 150 kcal no deben sobrepasar las 120…`
  - `Habilitado`: `NO`

### `sispro_tipo_programa_salud_covid`  ·  5 filas  ·  3.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoProgramaSaludCOVID>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:23Z  ·  sha256 `8dc0723a90ff…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoProgramaSaludCOVID`
  - `Codigo`: `01`
  - `Nombre`: `Técnico`
  - `Descripcion`: `Técnico`
  - `Habilitado`: `SI`

### `sispro_tv_sociedad_cientifica`  ·  110 filas  ·  68.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TVSociedadCientifica>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:23Z  ·  sha256 `76e6aed6a1bb…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TVSociedadCientifica`
  - `Codigo`: `SC00`
  - `Nombre`: `Ninguna`
  - `Descripcion`: ``
  - `Habilitado`: `SI`


## RIPS — auditoría / validación de reportes

### `sispro_estado_evolucion`  ·  9 filas  ·  6.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EstadoEvolucion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:57Z  ·  sha256 `e66a1a76ee8a…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EstadoEvolucion`
  - `Codigo`: `CAN`
  - `Nombre`: `Identificación Cancelada`
  - `Descripcion`: `Identificación Cancelada`
  - `Habilitado`: `SI`

### `sispro_finalidad_sexo_edad`  ·  34 filas  ·  22.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FinalidadSexoEdad>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:58Z  ·  sha256 `4e94da826743…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Finalidad`, `Extra_II:Sexo`, `Extra_III:Edad_INI`, `Extra_IV:Edad_FIN`
  `Extra_V:Consultas`, `Extra_VI:Procedimientos`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FinalidadSexoEdad`
  - `Codigo`: `1`
  - `Nombre`: `aa`
  - `Descripcion`: `aa`
  - `Habilitado`: `SI`

### `sispro_unirs`  ·  915 filas  ·  735.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=UNIRS>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:59Z  ·  sha256 `ce59902f099a…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:DCIConcentracion`, `Extra_II:FormaFarmaceutica`, `Extra_III:Indicaciones`, `Extra_IV:TipoIndicacion`
  `Extra_V:FechaModificacionIndicaciones`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `UNIRS`
  - `Codigo`: `0001`
  - `Nombre`: `ACIDO ALENDRONICO`
  - `Descripcion`: `[ACIDO ALENDRONICO] 10mg/1U`
  - `Habilitado`: `SI`


## Financiero (recobros, PILA, ARL, CCF, pagos, subsidios)

### `sispro_aco_ciiu`  ·  8 filas  ·  5.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOCiiu>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:24Z  ·  sha256 `6a0f0169fd28…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ACOCiiu`
  - `Codigo`: `941`
  - `Nombre`: `Actividades de asociaciones empresariales y de empleadores y asociaciones pro…`
  - `Descripcion`: `Actividades de asociaciones`
  - `Habilitado`: `SI`

### `sispro_aco_entidad_autorizada`  ·  203 filas  ·  174.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOEntidadAutorizada>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:25Z  ·  sha256 `6e1d3d55c28a…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Departamento`, `Extra_II:Municipio`, `Extra_III:Dirección`, `Extra_IV:Teléfono`
  `Extra_V:Correo`, `Extra_VI:Representante`, `Extra_VII:No. Resolución`, `Extra_VIII:Fecha de resolución`, `Extra_IX:Observación`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ACOEntidadAutorizada`
  - `Codigo`: `800020449`
  - `Nombre`: `HERMANASBETHLEMITASPROVINCIADELSAGRADOCORAZÓNDEJESÚS`
  - `Descripcion`: `EntidadAutorizada`
  - `Habilitado`: `SI`

### `sispro_aco_tipo_entidad`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOTipoEntidad>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:25Z  ·  sha256 `542692942576…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ACOTipoEntidad`
  - `Codigo`: `1`
  - `Nombre`: `Agremiación`
  - `Descripcion`: `Tipo de entidad`
  - `Habilitado`: `SI`

### `sispro_aco_tipo_entidad_reserva`  ·  2 filas  ·  1.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOTipoEntidadReserva>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:26Z  ·  sha256 `932514b17628…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ACOTipoEntidadReserva`
  - `Codigo`: `1`
  - `Nombre`: `Entidad financiera`
  - `Descripcion`: `Tipo de entidad donde se tiene constituida la reserva especial de garantía mí…`
  - `Habilitado`: `SI`

### `sispro_aco_tipo_persona`  ·  3 filas  ·  2.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOTipoPersona>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:26Z  ·  sha256 `61029f3cca4a…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ACOTipoPersona`
  - `Codigo`: `1`
  - `Nombre`: `Representante Legal`
  - `Descripcion`: `Tipo de persona que certifica la reserva especial de garantía mínima`
  - `Habilitado`: `SI`

### `sispro_aco_tipo_producto`  ·  6 filas  ·  4.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOTipoProducto>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:27Z  ·  sha256 `059af82688d4…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ACOTipoProducto`
  - `Codigo`: `1`
  - `Nombre`: `Cuenta de ahorro`
  - `Descripcion`: `Tipo de producto donde se constituyó la reserva especial de garantía mínima`
  - `Habilitado`: `SI`

### `sispro_aco_tipo_soporte_seguimiento`  ·  6 filas  ·  4.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ACOTipoSoporteSeguimiento>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:27Z  ·  sha256 `9e1caca74e15…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ACOTipoSoporteSeguimiento`
  - `Codigo`: `D20`
  - `Nombre`: `Concepto técnico y financiero`
  - `Descripcion`: `Tipo de documento al cual corresponde el soporte digitalizado`
  - `Habilitado`: `SI`

### `sispro_afp`  ·  16 filas  ·  10.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=AFP>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:28Z  ·  sha256 `39e42eb01b51…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `AFP`
  - `Codigo`: `230201`
  - `Nombre`: `PROTECCION`
  - `Descripcion`: `Administradora de Fondos de Pensiones y Cesantía Protección S.A.`
  - `Habilitado`: `SI`

### `sispro_arl`  ·  10 filas  ·  6.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ARL>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:28Z  ·  sha256 `c7d9a24aa6cc…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ARL`
  - `Codigo`: `14-04`
  - `Nombre`: `COLPATRIA`
  - `Descripcion`: `SEGUROS DE VIDA COLPATRIA S.A.`
  - `Habilitado`: `SI`

### `sispro_arl_estado_pago`  ·  4 filas  ·  3.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ARLEstadoPago>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:29Z  ·  sha256 `da8e1aed7471…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ARLEstadoPago`
  - `Codigo`: `1`
  - `Nombre`: `AlDia`
  - `Descripcion`: `Pago de aportes al SGRL al dia`
  - `Habilitado`: `SI`

### `sispro_arl_tipo_aportante`  ·  11 filas  ·  7.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ARLTipoAportante>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:29Z  ·  sha256 `a7d7c16d8a8e…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ARLTipoAportante`
  - `Codigo`: `1`
  - `Nombre`: `Empleador`
  - `Descripcion`: `Empleador`
  - `Habilitado`: `SI`

### `sispro_ccf_estado_pago`  ·  2 filas  ·  1.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CCFEstadoPago>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:30Z  ·  sha256 `ba152a371d9e…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CCFEstadoPago`
  - `Codigo`: `1`
  - `Nombre`: `Al día`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cma_indicador_registro_sustitucion`  ·  2 filas  ·  1.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMAIndicadorRegistroSustitucion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:30Z  ·  sha256 `cacfc581aed6…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CMAIndicadorRegistroSustitucion`
  - `Codigo`: `R`
  - `Nombre`: `R Registro de cuenta maestra`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cma_modalidad_subsidio`  ·  3 filas  ·  2.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMAModalidadSubsidio>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:31Z  ·  sha256 `6c035075dac7…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CMAModalidadSubsidio`
  - `Codigo`: `SP`
  - `Nombre`: `SP Subsidio Parcial`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cma_novedad`  ·  3 filas  ·  2.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMANovedad>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:31Z  ·  sha256 `ab875e33a77a…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CMANovedad`
  - `Codigo`: `E`
  - `Nombre`: `E Eliminacion de un beneficiario de una subcuenta maestra`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cma_sistema_pago`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMASistemaPago>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:32Z  ·  sha256 `2770f033dc17…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CMASistemaPago`
  - `Codigo`: `1`
  - `Nombre`: `1 ACH-CENIT`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cma_tipo_cuenta_bancaria`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMATipoCuentaBancaria>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:32Z  ·  sha256 `c66577bfcae8…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CMATipoCuentaBancaria`
  - `Codigo`: `A`
  - `Nombre`: `Cuenta de Ahorros`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cma_tipo_cuenta_maestra`  ·  6 filas  ·  4.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMATipoCuentaMaestra>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:33Z  ·  sha256 `770cc4ecc750…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CMATipoCuentaMaestra`
  - `Codigo`: `EP`
  - `Nombre`: `EP CTA MAESTRA de EPS`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cma_tipo_movimiento`  ·  5 filas  ·  3.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMATipoMovimiento>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:33Z  ·  sha256 `9abf035458dd…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CMATipoMovimiento`
  - `Codigo`: `E1`
  - `Nombre`: `E1 Egreso sin beneficiario`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cmh_tipo_cuenta_maestra`  ·  24 filas  ·  15.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMHTipoCuentaMaestra>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:34Z  ·  sha256 `c5a3d017840e…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CMHTipoCuentaMaestra`
  - `Codigo`: `AB`
  - `Nombre`: `PagadoraAgua`
  - `Descripcion`: `PagadoraAgua`
  - `Habilitado`: `SI`

### `sispro_cmh_tipo_movimiento`  ·  7 filas  ·  4.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMHTipoMovimiento>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:34Z  ·  sha256 `77767b9699d4…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CMHTipoMovimiento`
  - `Codigo`: `100`
  - `Nombre`: `ingreso`
  - `Descripcion`: `ingreso`
  - `Habilitado`: `SI`

### `sispro_cmh_tipo_movimiento_pg`  ·  22 filas  ·  14.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMHTipoMovimientoPG>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:35Z  ·  sha256 `11c446aa565a…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CMHTipoMovimientoPG`
  - `Codigo`: `100`
  - `Nombre`: `ingreso`
  - `Descripcion`: `ingreso`
  - `Habilitado`: `SI`

### `sispro_cmr_sistema_pago`  ·  4 filas  ·  2.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMRSistemaPago>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:35Z  ·  sha256 `e71eceba4d3c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CMRSistemaPago`
  - `Codigo`: `1`
  - `Nombre`: `ACH_CENIT`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cmr_tipo_cuenta_maestra`  ·  2 filas  ·  1.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMRTipoCuentaMaestra>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:36Z  ·  sha256 `6f9649f3b332…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CMRTipoCuentaMaestra`
  - `Codigo`: `01`
  - `Nombre`: `Asignaciones Directas`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cmv_tipo_movimiento`  ·  13 filas  ·  8.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CMVTipoMovimiento>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:36Z  ·  sha256 `f9c331f12a82…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CMVTipoMovimiento`
  - `Codigo`: `100`
  - `Nombre`: `Ingreso`
  - `Descripcion`: `Ingreso`
  - `Habilitado`: `SI`

### `sispro_eam_entidad_seguimiento`  ·  6 filas  ·  4.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EAMEntidadSeguimiento>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:37Z  ·  sha256 `5d29742ba0ae…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EAMEntidadSeguimiento`
  - `Codigo`: `01`
  - `Nombre`: `Secretaría de Salud`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_eam_jornada_atencion`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EAMJornadaAtencion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:37Z  ·  sha256 `ea22ed035f71…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EAMJornadaAtencion`
  - `Codigo`: `JC`
  - `Nombre`: `Jornada Continua`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_eam_nivel_ejecucion`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EAMNivelEjecucion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:38Z  ·  sha256 `28d778b9c5e4…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EAMNivelEjecucion`
  - `Codigo`: `01`
  - `Nombre`: `Nivel Departamental`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_eam_razon_no_ejecucion`  ·  3 filas  ·  2.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EAMRazonNoEjecucion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:39Z  ·  sha256 `39f946559af7…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EAMRazonNoEjecucion`
  - `Codigo`: `01`
  - `Nombre`: `No hay acto administrativo de 'Estampilla para el Bienestar del Adulto Mayor'`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_estado_recobro`  ·  4 filas  ·  2.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EstadoRecobro>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:39Z  ·  sha256 `93a0f9307ad5…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EstadoRecobro`
  - `Codigo`: `1`
  - `Nombre`: `APROBADO`
  - `Descripcion`: `RECOBRO APROBADO`
  - `Habilitado`: `SI`

### `sispro_factura_sin_contrato`  ·  6 filas  ·  5.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=facturaSinContrato>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:40Z  ·  sha256 `bc974e3f28f4…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:FechaInicioVigencia`, `Extra_II:FechaFinVigencia`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `facturaSinContrato`
  - `Codigo`: `01`
  - `Nombre`: `ATENCION DE URGENCIAS`
  - `Descripcion`: `ATENCION DE URGENCIAS`
  - `Habilitado`: `SI`

### `sispro_incapacidades_causal_contingencia`  ·  5 filas  ·  3.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesCausalContingencia>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:40Z  ·  sha256 `cb93111e1313…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IncapacidadesCausalContingencia`
  - `Codigo`: `1`
  - `Nombre`: `Dificultades técnicas`
  - `Descripcion`: `Dificultades técnicas`
  - `Habilitado`: `SI`

### `sispro_incapacidades_causal_dias_no_pagados`  ·  2 filas  ·  1.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesCausalDiasNoPagados>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:41Z  ·  sha256 `c9fdce5e55c8…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IncapacidadesCausalDiasNoPagados`
  - `Codigo`: `1`
  - `Nombre`: `Muerte de paciente`
  - `Descripcion`: `Muerte de paciente`
  - `Habilitado`: `SI`

### `sispro_incapacidades_causal_glosa`  ·  12 filas  ·  8.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesCausalGlosa>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:41Z  ·  sha256 `6d243fe571f5…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IncapacidadesCausalGlosa`
  - `Codigo`: `1`
  - `Nombre`: `Afiliado no cotizante`
  - `Descripcion`: `Afiliado no cotizante`
  - `Habilitado`: `SI`

### `sispro_incapacidades_concepto_rehabilitacion`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesConceptoRehabilitacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:42Z  ·  sha256 `7a311961890a…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IncapacidadesConceptoRehabilitacion`
  - `Codigo`: `1`
  - `Nombre`: `Favorable`
  - `Descripcion`: `Favorable`
  - `Habilitado`: `SI`

### `sispro_incapacidades_estado_pago`  ·  3 filas  ·  2.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesEstadoPago>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:42Z  ·  sha256 `ee181dbf8ee5…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IncapacidadesEstadoPago`
  - `Codigo`: `1`
  - `Nombre`: `Pagada`
  - `Descripcion`: `Pagada`
  - `Habilitado`: `SI`

### `sispro_incapacidades_grupos_servicios`  ·  5 filas  ·  3.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesGruposServicios>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:43Z  ·  sha256 `de020f72c909…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IncapacidadesGruposServicios`
  - `Codigo`: `1`
  - `Nombre`: `Consulta Externa`
  - `Descripcion`: `Consulta Externa`
  - `Habilitado`: `SI`

### `sispro_incapacidades_motivo_retroactividad`  ·  4 filas  ·  3.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesMotivoRetroactividad>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:43Z  ·  sha256 `6eb3e97dcbb6…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IncapacidadesMotivoRetroactividad`
  - `Codigo`: `1`
  - `Nombre`: `Internación del Paciente`
  - `Descripcion`: `Internación del Paciente`
  - `Habilitado`: `SI`

### `sispro_incapacidades_profesional_pcl`  ·  2 filas  ·  1.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesProfesionalPCL>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:44Z  ·  sha256 `211d2fc2960e…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IncapacidadesProfesionalPCL`
  - `Codigo`: `1`
  - `Nombre`: `Miembro de equipo calificador o juntas de calificación`
  - `Descripcion`: `Miembro de equipo calificador o juntas de calificación`
  - `Habilitado`: `SI`

### `sispro_incapacidades_tipo_evento_laboral`  ·  2 filas  ·  1.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesTipoEventoLaboral>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:44Z  ·  sha256 `370fa784f088…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IncapacidadesTipoEventoLaboral`
  - `Codigo`: `1`
  - `Nombre`: `Accidente de Trabajo`
  - `Descripcion`: `Accidente de Trabajo`
  - `Habilitado`: `SI`

### `sispro_incapacidades_tipo_pago`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IncapacidadesTipoPago>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:45Z  ·  sha256 `df5d3c058fe9…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IncapacidadesTipoPago`
  - `Codigo`: `1`
  - `Nombre`: `Normal`
  - `Descripcion`: `Normal`
  - `Habilitado`: `SI`

### `sispro_pila_causal_no_pago_electronico`  ·  4 filas  ·  3.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILACausalNoPagoElectronico>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:45Z  ·  sha256 `f124e2ac85dd…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PILACausalNoPagoElectronico`
  - `Codigo`: `1`
  - `Nombre`: `Prohibiciones_para_la_constitución_de_cuentas_bancarias`
  - `Descripcion`: `Prohibiciones para la constitución de cuentas bancarias`
  - `Habilitado`: `SI`

### `sispro_pila_correcciones`  ·  2 filas  ·  1.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILACorrecciones>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:46Z  ·  sha256 `7206ad444cea…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PILACorrecciones`
  - `Codigo`: `A`
  - `Nombre`: `corresponde a la línea originalmente cancelada`
  - `Descripcion`: `corresponde a la línea originalmente cancelada`
  - `Habilitado`: `SI`

### `sispro_pila_cruce_personas`  ·  9 filas  ·  6.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILACrucePersonas>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:46Z  ·  sha256 `7a67ef6daa87…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PILACrucePersonas`
  - `Codigo`: `BEP`
  - `Nombre`: `Beneficios Economicos Periodicos`
  - `Descripcion`: `Beneficios Economicos Periodicos`
  - `Habilitado`: `SI`

### `sispro_pila_forma_presentacion`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILAFormaPresentacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:47Z  ·  sha256 `dc48e44270f6…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PILAFormaPresentacion`
  - `Codigo`: `S`
  - `Nombre`: `Sucursal`
  - `Descripcion`: `Sucursal`
  - `Habilitado`: `SI`

### `sispro_pila_identificador`  ·  2 filas  ·  1.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILAIdentificador>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:47Z  ·  sha256 `147b66483f9e…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PILAIdentificador`
  - `Codigo`: `1`
  - `Nombre`: `Si la planilla pertenece a un aportante`
  - `Descripcion`: `Si la planilla pertenece a un aportante`
  - `Habilitado`: `SI`

### `sispro_pila_indicador_decreto688`  ·  2 filas  ·  1.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILAIndicadorDecreto688>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:48Z  ·  sha256 `6c233247d7d4…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PILAIndicadorDecreto688`
  - `Codigo`: `0`
  - `Nombre`: `NO tiene Reducción de interes`
  - `Descripcion`: `NO tiene Reducción de interes`
  - `Habilitado`: `SI`

### `sispro_pila_indicador_tarifa_especial_pensiones`  ·  4 filas  ·  3.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILAIndicadorTarifaEspecialPensiones>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:48Z  ·  sha256 `affda595d093…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PILAIndicadorTarifaEspecialPensiones`
  - `Codigo`: `1`
  - `Nombre`: `Actividades de alto riesgo`
  - `Descripcion`: `Actividades de alto riesgo`
  - `Habilitado`: `SI`

### `sispro_pila_ingreso`  ·  3 filas  ·  2.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILAIngreso>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:49Z  ·  sha256 `b0435fbbbbb9…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PILAIngreso`
  - `Codigo`: `C`
  - `Nombre`: `ingresa a Cajas`
  - `Descripcion`: `ingresa a Cajas`
  - `Habilitado`: `SI`

### `sispro_pila_modalidad_planilla`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILAModalidadPlanilla>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:49Z  ·  sha256 `8e3f31013000…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PILAModalidadPlanilla`
  - `Codigo`: `1`
  - `Nombre`: `Electrónica`
  - `Descripcion`: `Planilla gestionada por modalidad electrónica`
  - `Habilitado`: `SI`

### `sispro_pila_retiro`  ·  4 filas  ·  2.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PILARetiro>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:50Z  ·  sha256 `879cfb4192c4…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PILARetiro`
  - `Codigo`: `C`
  - `Nombre`: `Retira de Cajas`
  - `Descripcion`: `Retira de Cajas`
  - `Habilitado`: `SI`

### `sispro_rec_ambito_atencion`  ·  5 filas  ·  3.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECAmbitoAtencion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:50Z  ·  sha256 `64d5d59c5931…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RECAmbitoAtencion`
  - `Codigo`: `1`
  - `Nombre`: `Ambulatorio No Priorizado`
  - `Descripcion`: `Código ámbito de atención`
  - `Habilitado`: `SI`

### `sispro_rec_causa_negacion`  ·  40 filas  ·  27.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECCausaNegacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:51Z  ·  sha256 `0ea3497455bb…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RECCausaNegacion`
  - `Codigo`: `1`
  - `Nombre`: `Es un servicio o tecnología que tiene como finalidad principal un propósito c…`
  - `Descripcion`: `Causa de negación`
  - `Habilitado`: `SI`

### `sispro_rec_causa_no_entrega`  ·  16 filas  ·  10.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECCausaNoEntrega>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:52Z  ·  sha256 `fb902cf71e2d…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RECCausaNoEntrega`
  - `Codigo`: `1`
  - `Nombre`: `Misma solicitud en otra prescripcion`
  - `Descripcion`: `Causa de no entrega`
  - `Habilitado`: `SI`

### `sispro_rec_codigo_servicio_no_financiado`  ·  55 filas  ·  36.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECCodigoServicioNoFinanciado>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:52Z  ·  sha256 `515e179d0bb7…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RECCodigoServicioNoFinanciado`
  - `Codigo`: `01`
  - `Nombre`: `ACEITES (VEGETALES, ANIMALES, MINERALES)`
  - `Descripcion`: `Servicios No financiados`
  - `Habilitado`: `SI`

### `sispro_rec_concepto_negacion_servicio`  ·  2 filas  ·  1.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECConceptoNegacionServicio>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:53Z  ·  sha256 `c00372d423e9…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RECConceptoNegacionServicio`
  - `Codigo`: `NEG`
  - `Nombre`: `Servicio o tecnología ordenado por el médico tratante y negado por el CTC`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_rec_motivo_neg_ctc`  ·  10 filas  ·  7.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECMotivoNegCTC>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:53Z  ·  sha256 `e4e78bcc1a30…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RECMotivoNegCTC`
  - `Codigo`: `1`
  - `Nombre`: `El servicio solicitado es cobertura del POS`
  - `Descripcion`: `Motivo de negacion por el CTC (NEG)`
  - `Habilitado`: `SI`

### `sispro_rec_motivo_ntr_ctc`  ·  8 filas  ·  6.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECMotivoNtrCTC>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:54Z  ·  sha256 `a461a5dbb9ea…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RECMotivoNtrCTC`
  - `Codigo`: `1`
  - `Nombre`: `El servicio solicitado es cobertura del Plan de Beneficios con cargo a la UPC`
  - `Descripcion`: `Motivo para no haber tramitado la solicitud ante el CTC (NTR)`
  - `Habilitado`: `SI`

### `sispro_rec_servicios_especificos_no_pos`  ·  12 filas  ·  8.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECServiciosEspecificosNoPos>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:54Z  ·  sha256 `d4eba0449d80…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RECServiciosEspecificosNoPos`
  - `Codigo`: `108`
  - `Nombre`: `BLOQUEADORES SOLARES`
  - `Descripcion`: `Servicios Especificos No Pos`
  - `Habilitado`: `SI`

### `sispro_rec_tipo_servicio`  ·  6 filas  ·  4.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RECTipoServicio>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:55Z  ·  sha256 `74a019111687…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Codigonumerico`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RECTipoServicio`
  - `Codigo`: `C`
  - `Nombre`: `Servicios no financiados con recursos de salud`
  - `Descripcion`: `Tipo de servicio solicitado`
  - `Habilitado`: `SI`

### `sispro_sgd01221`  ·  4 filas  ·  2.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGD01221>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:55Z  ·  sha256 `5ef443080227…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SGD01221`
  - `Codigo`: `0`
  - `Nombre`: `No aplica`
  - `Descripcion`: `No aplica`
  - `Habilitado`: `SI`

### `sispro_sgd012321`  ·  5 filas  ·  3.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGD012321>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:56Z  ·  sha256 `ca4f64d0270b…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SGD012321`
  - `Codigo`: `0`
  - `Nombre`: `No aplica`
  - `Descripcion`: `No aplica`
  - `Habilitado`: `SI`

### `sispro_sgd034521`  ·  5 filas  ·  3.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGD034521>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:56Z  ·  sha256 `ee8f6b77fbdf…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SGD034521`
  - `Codigo`: `0`
  - `Nombre`: `0`
  - `Descripcion`: `0`
  - `Habilitado`: `SI`

### `sispro_sgd045621`  ·  5 filas  ·  3.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGD045621>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:57Z  ·  sha256 `7e8d0b58d8d7…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SGD045621`
  - `Codigo`: `0`
  - `Nombre`: `0`
  - `Descripcion`: `0`
  - `Habilitado`: `SI`

### `sispro_sgd067891021`  ·  7 filas  ·  4.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGD067891021>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:57Z  ·  sha256 `fb0af6651eaa…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SGD067891021`
  - `Codigo`: `0`
  - `Nombre`: `0`
  - `Descripcion`: `0`
  - `Habilitado`: `SI`

### `sispro_sgd1221`  ·  3 filas  ·  2.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGD1221>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:58Z  ·  sha256 `63900c100007…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SGD1221`
  - `Codigo`: `1`
  - `Nombre`: `Si`
  - `Descripcion`: `Si`
  - `Habilitado`: `SI`

### `sispro_sgd_actividad`  ·  70 filas  ·  44.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGDActividad>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:59Z  ·  sha256 `885dddf294cd…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SGDActividad`
  - `Codigo`: `0`
  - `Nombre`: `Dosis BCG`
  - `Descripcion`: `Dosis BCG`
  - `Habilitado`: `SI`

### `sispro_sgd_actividades_nomin`  ·  73 filas  ·  47.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGDActividadesNomin>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:14:59Z  ·  sha256 `f72781e91f0f…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SGDActividadesNomin`
  - `Codigo`: `0`
  - `Nombre`: `Dosis BCG`
  - `Descripcion`: `Dosis BCG`
  - `Habilitado`: `SI`

### `sispro_sgd_ambito_prestacion`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGDAmbitoPrestacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:00Z  ·  sha256 `b9140f0758a2…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SGDAmbitoPrestacion`
  - `Codigo`: `0`
  - `Nombre`: `Intramural`
  - `Descripcion`: `Intramural`
  - `Habilitado`: `SI`

### `sispro_sgd_baciloscopia_diag`  ·  6 filas  ·  4.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGDBaciloscopiaDiag>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:00Z  ·  sha256 `9bd9fd0bf34f…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SGDBaciloscopiaDiag`
  - `Codigo`: `1`
  - `Nombre`: `Negativa`
  - `Descripcion`: `Negativa`
  - `Habilitado`: `SI`

### `sispro_sgd_cal_muestra_cit_cer`  ·  6 filas  ·  4.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SGDCalMuestraCitCer>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:01Z  ·  sha256 `ecc2889fb0e1…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SGDCalMuestraCitCer`
  - `Codigo`: `0`
  - `Nombre`: `No aplica`
  - `Descripcion`: `No aplica`
  - `Habilitado`: `SI`

### `sispro_siem_causa_entrega_incompleta`  ·  7 filas  ·  5.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SIEMCausaEntregaIncompleta>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:01Z  ·  sha256 `1e701039416b…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SIEMCausaEntregaIncompleta`
  - `Codigo`: `AE`
  - `Nombre`: `Autorización, prescripción o transcripción errada`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_siem_causa_no_entrega`  ·  2 filas  ·  2.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SIEMCausaNoEntrega>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:02Z  ·  sha256 `590bd91aa3bf…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SIEMCausaNoEntrega`
  - `Codigo`: `1`
  - `Nombre`: `El afiliado se reusa a recibir los medicamentos al momento de efectuar el mec…`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_siem_profesion_quien_entrega`  ·  3 filas  ·  2.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SIEMProfesionQuienEntrega>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:03Z  ·  sha256 `dec1132a75b0…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SIEMProfesionQuienEntrega`
  - `Codigo`: `OT`
  - `Nombre`: `Otro`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_siem_sitio_entrega`  ·  4 filas  ·  3.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SIEMSitioEntrega>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:03Z  ·  sha256 `bcec37c82550…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SIEMSitioEntrega`
  - `Codigo`: `D`
  - `Nombre`: `Establecimiento farmacéutico diferente de donde realilza la reclamación inici…`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_siem_via_autorizacion_entrega`  ·  4 filas  ·  3.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SIEMViaAutorizacionEntrega>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:03Z  ·  sha256 `9a74bb325fb1…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SIEMViaAutorizacionEntrega`
  - `Codigo`: `1`
  - `Nombre`: `Prescripcion`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipo_recobro`  ·  2 filas  ·  1.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoRecobro>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:04Z  ·  sha256 `c79ca396ce45…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoRecobro`
  - `Codigo`: `P`
  - `Nombre`: `PRESCRIPCION`
  - `Descripcion`: `RECOBRO POR PRESCRIPCION`
  - `Habilitado`: `SI`


## Administrativo / demografía (tipos de ID, sexo, ocupación, régimen, afiliación)

### `sispro_cobertura_plan`  ·  15 filas  ·  10.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=coberturaPlan>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:00Z  ·  sha256 `a3e5c66f57dd…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:TipoUsuario`, `Extra_II:ModalidadPago`, `Extra_III:ConceptoRecaudo`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `coberturaPlan`
  - `Codigo`: `01`
  - `Nombre`: `Plan de beneficios en salud financiado con UPC`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cobertura_plan_usuario`  ·  24 filas  ·  15.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CoberturaPlanUsuario>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:00Z  ·  sha256 `11e67989d311…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:CoberturaPlan`, `Extra_II:TipoUsuario`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CoberturaPlanUsuario`
  - `Codigo`: `01`
  - `Nombre`: `relacion1`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cpti_tipo_poblacion`  ·  5 filas  ·  3.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTITipoPoblacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:01Z  ·  sha256 `44efc3cdc7cb…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CPTITipoPoblacion`
  - `Codigo`: `1`
  - `Nombre`: `Indigena`
  - `Descripcion`: `CPTI Tipo Poblacion Pertenece Indigena`
  - `Habilitado`: `SI`

### `sispro_eps_volumen_afiliados`  ·  103 filas  ·  63.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EPSVolumenAfiliados>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:01Z  ·  sha256 `463664fbd116…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Nit`, `Extra_II:Afiliados`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EPSVolumenAfiliados`
  - `Codigo`: `BDEX`
  - `Nombre`: `BDEX`
  - `Descripcion`: `BDEX`
  - `Habilitado`: `SI`

### `sispro_etnia`  ·  6 filas  ·  4.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Etnia>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:02Z  ·  sha256 `41d107e62d29…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `Etnia`
  - `Codigo`: `1`
  - `Nombre`: `Indigena`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_lce_novedad_eliminacion`  ·  44 filas  ·  31.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LCENovedadEliminacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:02Z  ·  sha256 `e77b9c3c1ae9…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:FechaCorte`, `Extra_II:TipoIDEntidad`, `Extra_III:NroIdEntidad`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `LCENovedadEliminacion`
  - `Codigo`: `20230111_1`
  - `Nombre`: `Novedad Eliminación`
  - `Descripcion`: `Activar Novedad Eliminación por fecha de corte`
  - `Habilitado`: `NO`

### `sispro_lce_responsables_envio_informacion_por_tipo_poblacion_especial`  ·  42 filas  ·  37.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LCEResponsablesEnvioInformacionPorTipoPoblacionEspecial>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:03Z  ·  sha256 `a6fb94210cbb…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:TipoIDEntidad`, `Extra_II:NroIdEntidad`, `Extra_III:TipoPoblacionEspecial`, `Extra_IV:NombrePoblacionEspecial`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `LCEResponsablesEnvioInformacionPorTipoPoblacionEspecial`
  - `Codigo`: `101`
  - `Nombre`: `Municipio`
  - `Descripcion`: `LCE Responsables Envío Información Por Tipo Población Especial en el Municipio`
  - `Habilitado`: `SI`

### `sispro_lce_tipo_poblacion_especial`  ·  21 filas  ·  15.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LCETipoPoblacionEspecial>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:03Z  ·  sha256 `1caef285fc89…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `LCETipoPoblacionEspecial`
  - `Codigo`: `1`
  - `Nombre`: `Población Habitante de calle`
  - `Descripcion`: `Tipo de Población Especial del Régimen Subsidiado`
  - `Habilitado`: `SI`

### `sispro_orientacion_sexual`  ·  5 filas  ·  3.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=OrientacionSexual>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:04Z  ·  sha256 `d594ff5d312b…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `orientacionsexual`
  - `Codigo`: `1`
  - `Nombre`: `Lesbiana`
  - `Descripcion`: `Lesbiana`
  - `Habilitado`: `SI`

### `sispro_pai_tipo_id_nacido_vivo`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PAITipoIDNacidoVivo>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:04Z  ·  sha256 `e4b8cc71cca8…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PAITipoIDNacidoVivo`
  - `Codigo`: `RC`
  - `Nombre`: `Registro civil`
  - `Descripcion`: `Registro civil`
  - `Habilitado`: `SI`

### `sispro_pro170_regimen_salud`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PRO170RegimenSalud>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:05Z  ·  sha256 `46bec891feb0…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PRO170RegimenSalud`
  - `Codigo`: `1`
  - `Nombre`: `SUBSIDIADO`
  - `Descripcion`: `SUBSIDIADO`
  - `Habilitado`: `SI`

### `sispro_psracausretivincbenef`  ·  6 filas  ·  4.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRACAUSRETIVINCBENEF>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:06Z  ·  sha256 `348e43f52c3c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PSRACAUSRETIVINCBENEF`
  - `Codigo`: `1`
  - `Nombre`: `Finalización del Programa`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_psraestadobenefi`  ·  6 filas  ·  4.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRAESTADOBENEFI>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:06Z  ·  sha256 `6c75841f19f1…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PSRAESTADOBENEFI`
  - `Codigo`: `1`
  - `Nombre`: `Otorgado`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_psratipobenefi`  ·  13 filas  ·  8.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRATIPOBENEFI>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:07Z  ·  sha256 `3d8fafb61c9e…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PSRATIPOBENEFI`
  - `Codigo`: `1`
  - `Nombre`: `Económico`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_psratiposubsid`  ·  5 filas  ·  3.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRATIPOSUBSID>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:07Z  ·  sha256 `d1ded6707cf1…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PSRATIPOSUBSID`
  - `Codigo`: `10`
  - `Nombre`: `Aprendices`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_psrccausretiafil`  ·  13 filas  ·  8.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRCCAUSRETIAFIL>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:08Z  ·  sha256 `750edcff0a73…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PSRCCAUSRETIAFIL`
  - `Codigo`: `1`
  - `Nombre`: `Desvinculacion del trabajador con el aportante`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_psrccondbeneccf`  ·  2 filas  ·  1.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRCCONDBENECCF>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:08Z  ·  sha256 `26d6686c1f74…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PSRCCONDBENECCF`
  - `Codigo`: `D`
  - `Nombre`: `Discapacitado`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_psrcestaafilccf`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRCESTAAFILCCF>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:09Z  ·  sha256 `4b31ca81218a…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PSRCESTAAFILCCF`
  - `Codigo`: `1`
  - `Nombre`: `Activo`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_psrcestadobenefi`  ·  5 filas  ·  3.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRCESTADOBENEFI>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:09Z  ·  sha256 `201b0b02d1df…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PSRCESTADOBENEFI`
  - `Codigo`: `1`
  - `Nombre`: `Otorgado`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_psrctipmiepobcub`  ·  3 filas  ·  2.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRCTIPMIEPOBCUB>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:10Z  ·  sha256 `521637db5d4c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PSRCTIPMIEPOBCUB`
  - `Codigo`: `1`
  - `Nombre`: `Afiliado`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_psrctipoafilccf`  ·  7 filas  ·  4.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSRCTIPOAFILCCF>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:10Z  ·  sha256 `cd67cbc3c2bd…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PSRCTIPOAFILCCF`
  - `Codigo`: `1`
  - `Nombre`: `Trabajador afiliado dependiente`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_riba_actividad_economica`  ·  17 filas  ·  11.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBAActividadEconomica>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:11Z  ·  sha256 `2fdfee54fdd7…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RIBAActividadEconomica`
  - `Codigo`: `1`
  - `Nombre`: `Agricultura Caza o Pesca`
  - `Descripcion`: `Agricultura Caza o Pesca`
  - `Habilitado`: `SI`

### `sispro_riba_nivel_educativo`  ·  6 filas  ·  4.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBANivelEducativo>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:11Z  ·  sha256 `979bcddb0bfb…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RIBANivelEducativo`
  - `Codigo`: `0`
  - `Nombre`: `Sin Nivel Educativo`
  - `Descripcion`: `Sin Nivel Educativo`
  - `Habilitado`: `SI`

### `sispro_riba_nivel_sisben`  ·  4 filas  ·  2.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBANivelSISBEN>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:12Z  ·  sha256 `4cd807e3d4e4…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RIBANivelSISBEN`
  - `Codigo`: `1`
  - `Nombre`: `Nivel I`
  - `Descripcion`: `Nivel I`
  - `Habilitado`: `SI`

### `sispro_riba_novedad_ingreso_modificacion`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBANovedadIngresoModificacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:12Z  ·  sha256 `c976797bb164…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RIBANovedadIngresoModificacion`
  - `Codigo`: `I`
  - `Nombre`: `Ingreso`
  - `Descripcion`: `Ingreso`
  - `Habilitado`: `SI`

### `sispro_riba_parentesco_cotizante`  ·  8 filas  ·  5.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBAParentescoCotizante>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:13Z  ·  sha256 `581c5fa1d576…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RIBAParentescoCotizante`
  - `Codigo`: `1`
  - `Nombre`: `Conyuge o compañero(a) permanente`
  - `Descripcion`: `Conyuge o compañero(a) permanente`
  - `Habilitado`: `SI`

### `sispro_riba_tipo_afiliado`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBATipoAfiliado>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:13Z  ·  sha256 `7b4497867880…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RIBATipoAfiliado`
  - `Codigo`: `A`
  - `Nombre`: `Adicional`
  - `Descripcion`: `Adicional`
  - `Habilitado`: `SI`

### `sispro_riba_tipo_cotizante`  ·  4 filas  ·  3.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBATipoCotizante>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:14Z  ·  sha256 `4732082b9a07…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RIBATipoCotizante`
  - `Codigo`: `16`
  - `Nombre`: `Independiente agremiado o asociado`
  - `Descripcion`: `Independiente agremiado o asociado`
  - `Habilitado`: `SI`

### `sispro_riba_tipo_vivienda`  ·  4 filas  ·  2.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=RIBATipoVivienda>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:14Z  ·  sha256 `74205cc5fbe3…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `RIBATipoVivienda`
  - `Codigo`: `1`
  - `Nombre`: `Propia`
  - `Descripcion`: `Propia`
  - `Habilitado`: `SI`

### `sispro_saa_tipo_novedad`  ·  18 filas  ·  11.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SAATipoNovedad>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:15Z  ·  sha256 `3f8b64c7a435…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SAATipoNovedad`
  - `Codigo`: `AVP`
  - `Nombre`: `Aporte Voluntario`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tenencia_hogar`  ·  5 filas  ·  3.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TenenciaHogar>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:15Z  ·  sha256 `1402b248daf3…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:TenenciaHogar`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TenenciaHogar`
  - `Codigo`: `1`
  - `Nombre`: `En arriendo o subarriendo`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipo_entidad_giro_subsidiado`  ·  2 filas  ·  1.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoEntidadGiroSubsidiado>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:16Z  ·  sha256 `291269a9d962…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoEntidadGiroSubsidiado`
  - `Codigo`: `IPS`
  - `Nombre`: `IPS Tipo de Entidad IPS para  la cual se permite Giro directo de Régimen Subs…`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipo_entidad_reporta_incapacidad`  ·  4 filas  ·  3.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoEntidadReportaIncapacidad>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:16Z  ·  sha256 `7181cc0f664b…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoEntidadReportaIncapacidad`
  - `Codigo`: `A`
  - `Nombre`: `ARL`
  - `Descripcion`: `ARL`
  - `Habilitado`: `SI`

### `sispro_tipo_estandar_id_internacional`  ·  5 filas  ·  3.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoEstandarIDInternacional>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:17Z  ·  sha256 `909d2991105a…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoEstandarIDInternacional`
  - `Codigo`: `1`
  - `Nombre`: `EAN 8/GTIN 8`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipo_estandar_para_cantidad_y_unidad_medida`  ·  33 filas  ·  24.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoEstandarParaCantidadYUnidadMedida>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:17Z  ·  sha256 `a5703e464e38…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoEstandarParaCantidadYUnidadMedida`
  - `Codigo`: `1`
  - `Nombre`: `POR UNIDAD, EN FORMAS DE PRESENTACION DOSIFICADA,  EN  CASO  DE  TABLETAS,  C…`
  - `Descripcion`: ``
  - `Habilitado`: `NO`

### `sispro_tipo_id_afiliado_rs`  ·  11 filas  ·  7.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDAfiliadoRS>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:18Z  ·  sha256 `4757e5aa8c54…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoIDAfiliadoRS`
  - `Codigo`: `AS`
  - `Nombre`: `Adulto sin identificación`
  - `Descripcion`: `Tipo de documento de Identificación  del usuario`
  - `Habilitado`: `SI`

### `sispro_tipo_id_aportante`  ·  9 filas  ·  6.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDAportante>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:18Z  ·  sha256 `59d9967d4f50…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoIDAportante`
  - `Codigo`: `CC`
  - `Nombre`: `Cédula de ciudadanía`
  - `Descripcion`: `Cédula de ciudadanía`
  - `Habilitado`: `SI`

### `sispro_tipo_id_cotizante`  ·  6 filas  ·  4.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDCotizante>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:19Z  ·  sha256 `2e48b6bcb1b6…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoIDCotizante`
  - `Codigo`: `CC`
  - `Nombre`: `CC Cédula Ciudadanía`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipo_id_demo`  ·  2 filas  ·  1.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIdDemo>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:19Z  ·  sha256 `3c7193b93f77…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoIdDemo`
  - `Codigo`: `MS`
  - `Nombre`: `Menor sin identificación`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipo_id_empleador`  ·  5 filas  ·  3.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDEmpleador>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:20Z  ·  sha256 `4349fe810842…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:LongitudMin`, `Extra_II:LongitudMax`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoIDEmpleador`
  - `Codigo`: `CC`
  - `Nombre`: `Cédula de ciudadanía`
  - `Descripcion`: ``
  - `Habilitado`: `NO`

### `sispro_tipo_id_sisdis`  ·  5 filas  ·  3.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIdSISDIS>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:20Z  ·  sha256 `ab181ef3ce6d…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoIdSISDIS`
  - `Codigo`: `DE`
  - `Nombre`: `Departamento`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipo_idrccnms`  ·  5 filas  ·  3.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDRCCNMS>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:21Z  ·  sha256 `48a4f0d5e88f…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoIDRCCNMS`
  - `Codigo`: `CN`
  - `Nombre`: `CN Certificado Nacido Vivo`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipo_idrcpa`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDRCPA>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:21Z  ·  sha256 `0ef9cde03ccf…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoIDRCPA`
  - `Codigo`: `PA`
  - `Nombre`: `Pasaporte`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipo_idrctipa`  ·  4 filas  ·  2.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIDRCTIPA>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:22Z  ·  sha256 `13749f1ac296…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoIDRCTIPA`
  - `Codigo`: `PA`
  - `Nombre`: `Pasaporte`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipo_incapacidad`  ·  5 filas  ·  3.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoIncapacidad>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:22Z  ·  sha256 `c618c093085e…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoIncapacidad`
  - `Codigo`: `1`
  - `Nombre`: `inicial`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipo_personal`  ·  61 filas  ·  37.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoPersonal>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:23Z  ·  sha256 `5883d96d7112…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoPersonal`
  - `Codigo`: `01`
  - `Nombre`: `Custodia y vigilancia`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipo_salario_afiliado`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipoSalarioAfiliado>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:23Z  ·  sha256 `026a3e8b8181…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipoSalarioAfiliado`
  - `Codigo`: `1`
  - `Nombre`: `Fijo`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tipologia_ebs`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TipologiaEBS>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T20:54:24Z  ·  sha256 `842ec1c3f25c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TipologiaEBS`
  - `Codigo`: `1`
  - `Nombre`: `Equipo Básico de Salud`
  - `Descripcion`: ``
  - `Habilitado`: `SI`


## Geografía (DIVIPOLA, postales, vías, países)

### `codigos_postales`  ·  3,681 filas  ·  2.2 MB

- **Kind**: `socrata`
- **URL**: <https://www.datos.gov.co/resource/ixig-z8b5.json>
- **Licencia**: Datos Abiertos Colombia (Ley 1712/2014)
- **Versión / sync**: 2025-05-20T20:24:15+00:00  ·  sha256 `c5962db0f984…`
- **Columnas** (14):
  `noid`, `codigo_departamento`, `nombre_departamento`, `codigo_municipio`, `nombre_municipio`, `zona_postal`
  `codigo_postal`, `limite_norte`, `limite_sur`, `limite_este`, `limite_oeste`, `tipo`
  `barrios_contenidos_en_el`, `veredas_contenidas_en_el`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `noid`: `877`
  - `codigo_departamento`: `15`
  - `nombre_departamento`: `BOYACA`
  - `codigo_municipio`: `15621`
  - `nombre_municipio`: `RONDON`

### `divipola_centros_poblados`  ·  8,161 filas  ·  2.7 MB

- **Kind**: `socrata`
- **URL**: <https://www.datos.gov.co/resource/xaxy-8nri.json>
- **Licencia**: Datos Abiertos Colombia (Ley 1712/2014)
- **Versión / sync**: 2025-01-24T21:14:58+00:00  ·  sha256 `2700c3fece2e…`
- **Columnas** (9):
  `codigo_departamento`, `nombre_departamento`, `codigo_municipio`, `nombre_municipio`, `codigo_centro_poblado`, `nombre_centro_poblado`
  `tipo_centro_poblado`, `longitud`, `latitud`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `codigo_departamento`: `05`
  - `nombre_departamento`: `ANTIOQUIA`
  - `codigo_municipio`: `05001`
  - `nombre_municipio`: `MEDELLÍN`
  - `codigo_centro_poblado`: `05001000`

### `divipola_departamentos`  ·  33 filas  ·  5.6 KB

- **Kind**: `socrata`
- **URL**: <https://www.datos.gov.co/resource/vcjz-niiq.json>
- **Licencia**: Datos Abiertos Colombia (Ley 1712/2014)
- **Versión / sync**: 2025-01-23T21:56:46+00:00  ·  sha256 `845dcf19f442…`
- **Columnas** (4):
  `codigo_departamento`, `nombre_departamento`, `longitud`, `latitud`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `codigo_departamento`: `05`
  - `nombre_departamento`: `ANTIOQUIA`
  - `longitud`: `-75,504557037`
  - `latitud`: `6,702032125`

### `divipola_municipios`  ·  1,122 filas  ·  240.5 KB

- **Kind**: `socrata`
- **URL**: <https://www.datos.gov.co/resource/gdxc-w37w.json>
- **Licencia**: Datos Abiertos Colombia (Ley 1712/2014)
- **Versión / sync**: 2025-01-24T20:44:32+00:00  ·  sha256 `5964193765e8…`
- **Columnas** (7):
  `cod_dpto`, `dpto`, `cod_mpio`, `nom_mpio`, `tipo_municipio`, `longitud`
  `latitud`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `cod_dpto`: `05`
  - `dpto`: `ANTIOQUIA`
  - `cod_mpio`: `05001`
  - `nom_mpio`: `MEDELLÍN`
  - `tipo_municipio`: `Municipio`

### `sispro_dmes_pais`  ·  249 filas  ·  146.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESPais>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:05Z  ·  sha256 `1ad60311913e…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `DMESPais`
  - `Codigo`: `10`
  - `Nombre`: `Antártida`
  - `Descripcion`: `Antártida`
  - `Habilitado`: `SI`

### `vias_invias`  ·  710 filas  ·  589.3 MB

- **Kind**: `socrata`
- **URL**: <https://www.datos.gov.co/resource/ie7y-asdn.json>
- **Licencia**: Datos Abiertos Colombia (Ley 1712/2014)
- **Versión / sync**: 2026-04-20T15:14:57+00:00  ·  sha256 `66fa16641bcf…`
- **Columnas** (18):
  `administrador`, `calzada`, `categoria`, `codigo_tramo`, `distancia_final`, `distancia_inicial`
  `fuente`, `grupo_administrador_vial`, `nombre_ruta`, `nombre_tramo`, `poste_de_referencia_final`, `poste_de_referencia_inicial`
  `ruta`, `sector`, `shape__length`, `superficie`, `territorial`, `multiline`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `administrador`: `1`
  - `calzada`: `1`
  - `categoria`: `2`
  - `codigo_tramo`: `55ST02`
  - `distancia_final`: `0`


## Misceláneos (demás tablas SISPRO sin categoría específica)

### `sispro_administradora_recuado_resolucion1715de2014`  ·  3 filas  ·  2.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=AdministradoraRecuadoResolucion1715de2014>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:13Z  ·  sha256 `b9cf5c84b918…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `AdministradoraRecuadoResolucion1715de2014`
  - `Codigo`: `MIN001`
  - `Nombre`: `cotizante no afiliado a EPS de contributivo o la EPS está en liquidación o co…`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_anexo_tecnico_nombre`  ·  255 filas  ·  174.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=AnexoTecnicoNombre>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:14Z  ·  sha256 `f6f876dab75c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:IDEsquema`, `Extra_II:NombreEsquema`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `AnexoTecnicoNombre`
  - `Codigo`: `ACO200IMAG`
  - `Nombre`: `ACO200IMAG`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_aplicacion`  ·  35 filas  ·  25.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Aplicacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:15Z  ·  sha256 `500cf83b89ac…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:URL Base PATH`, `Extra_II:TieneIndicadores`, `Extra_III:NombreAplicacionEnIndicadores`, `Extra_IV:AutorizaUsr`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `Aplicacion`
  - `Codigo`: `1`
  - `Nombre`: `SISMED - Sistema de Información de Precios de Medicamentos`
  - `Descripcion`: `SISMED - Sistema de Información de Precios de Medicamentos`
  - `Habilitado`: `SI`

### `sispro_asegurador_demo`  ·  37 filas  ·  23.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=AseguradorDemo>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:16Z  ·  sha256 `e1a8de6c5791…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `AseguradorDemo`
  - `Codigo`: `EPS001`
  - `Nombre`: `ALIANSALUD`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_campo_tabla_referencia`  ·  13 filas  ·  9.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CampoTablaReferencia>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:16Z  ·  sha256 `e96256ba5494…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CampoTablaReferencia`
  - `Codigo`: `Codigo`
  - `Nombre`: `Atributo Codigo`
  - `Descripcion`: `Atributo Codigo de tablas de referencia`
  - `Habilitado`: `SI`

### `sispro_cargo_dir_docentes`  ·  6 filas  ·  4.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CargoDirDocentes>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:17Z  ·  sha256 `c18be485af1c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CargoDirDocentes`
  - `Codigo`: `1`
  - `Nombre`: `Rector`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cargo_docente`  ·  9 filas  ·  5.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CargoDocente>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:17Z  ·  sha256 `53de759c9ac0…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CargoDocente`
  - `Codigo`: `1`
  - `Nombre`: `Docente de preescolar`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cargos_administrativos_edu`  ·  7 filas  ·  4.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CargosAdministrativosEdu>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:18Z  ·  sha256 `0a788738ca3d…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CargosAdministrativosEdu`
  - `Codigo`: `1`
  - `Nombre`: `Secretario(a)`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cargos_apoyo_edu`  ·  13 filas  ·  8.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CargosApoyoEdu>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:18Z  ·  sha256 `5232a5810587…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CargosApoyoEdu`
  - `Codigo`: `1`
  - `Nombre`: `Psicólogo`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_catalogo_expedientes_sismed`  ·  46,000 filas  ·  35.3 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CatalogoExpedientesSISMED>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:50Z  ·  sha256 `0ce09138374c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:POS`, `Extra_II:Cod_ATC`, `Extra_III:ATC`, `Extra_IV:RegistroSanitario`
  `Extra_V:ERSCodigo`, `Extra_VI:ERSNombre`, `Extra_VII:PrincipioActivo`, `Extra_VIII:ViaAdministracion`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CatalogoExpedientesSISMED`
  - `Codigo`: `10039`
  - `Nombre`: `SIN-SO POLVO`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_causal_no_pago`  ·  12 filas  ·  8.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CausalNoPago>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:50Z  ·  sha256 `f5d9000ec231…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CausalNoPago`
  - `Codigo`: `CNP01`
  - `Nombre`: `La EPS-S no presento el reporte de carnetizados de la continuidad`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_clase_triage`  ·  5 filas  ·  3.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ClaseTriage>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:51Z  ·  sha256 `4c35dba711df…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ClaseTriage`
  - `Codigo`: `01`
  - `Nombre`: `Triage I`
  - `Descripcion`: `Triage I`
  - `Habilitado`: `SI`

### `sispro_codigo_prepagadas`  ·  11 filas  ·  7.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CodigoPrepagadas>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:51Z  ·  sha256 `aa3871206d78…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CodigoPrepagadas`
  - `Codigo`: `EMP002`
  - `Nombre`: `MEDPLUS MEDICINA PREPAGADA S.A.`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_comodin0`  ·  1 filas  ·  1.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Comodin0>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:52Z  ·  sha256 `4892a3b931b6…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `Comodin0`
  - `Codigo`: `0`
  - `Nombre`: `0`
  - `Descripcion`: `Valor comodin 0`
  - `Habilitado`: `SI`

### `sispro_comodin00`  ·  1 filas  ·  1.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Comodin00>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:52Z  ·  sha256 `abcb78004bd9…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `Comodin00`
  - `Codigo`: `00`
  - `Nombre`: `No Aplica`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_comodin000`  ·  1 filas  ·  1.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Comodin000>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:53Z  ·  sha256 `df404083480d…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `Comodin000`
  - `Codigo`: `000`
  - `Nombre`: `No Aplica`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_comodin9999`  ·  2 filas  ·  1.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Comodin9999>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:54Z  ·  sha256 `cbbc1d253557…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `Comodin9999`
  - `Codigo`: `0000`
  - `Nombre`: `0000`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_con_victima`  ·  6 filas  ·  4.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ConVictima>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:54Z  ·  sha256 `8626df08c2a8…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ConVictima`
  - `Codigo`: `01`
  - `Nombre`: `Conductor`
  - `Descripcion`: `Conductor`
  - `Habilitado`: `SI`

### `sispro_concepto_recaudo`  ·  5 filas  ·  3.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=conceptoRecaudo>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:55Z  ·  sha256 `0e3040bb8fd5…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `conceptoRecaudo`
  - `Codigo`: `01`
  - `Nombre`: `COPAGO`
  - `Descripcion`: `COPAGO`
  - `Habilitado`: `SI`

### `sispro_condicion_beneficiario`  ·  2 filas  ·  1.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CondicionBeneficiario>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:55Z  ·  sha256 `c82fcbec63d0…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CondicionBeneficiario`
  - `Codigo`: `D`
  - `Nombre`: `Discapacitado`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_condicion_luz`  ·  2 filas  ·  1.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CondicionLuz>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:56Z  ·  sha256 `a06f1b0c9294…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CondicionLuz`
  - `Codigo`: `1`
  - `Nombre`: `NO CONTROLADA`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_cpti_actividad_economica`  ·  21 filas  ·  15.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIActividadEconomica>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:56Z  ·  sha256 `905ba7aa1df7…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CPTIActividadEconomica`
  - `Codigo`: `1`
  - `Nombre`: `AGRICULTURA, GANADERÍA, CAZA, SILVICULTURA Y PESCA`
  - `Descripcion`: `Actividades economica del oficio u ocupacion AGRICULTURA, GANADERÍA, CAZA Y A…`
  - `Habilitado`: `SI`

### `sispro_cpti_frecuencia`  ·  5 filas  ·  3.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIFrecuencia>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:57Z  ·  sha256 `cb70f6a6bb57…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CPTIFrecuencia`
  - `Codigo`: `1`
  - `Nombre`: `Diariamente`
  - `Descripcion`: `CPTI Frecuencia Diariamente`
  - `Habilitado`: `SI`

### `sispro_cpti_nivel_escolar`  ·  12 filas  ·  8.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTINivelEscolar>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:57Z  ·  sha256 `c50c13c12fa6…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CPTINivelEscolar`
  - `Codigo`: `1`
  - `Nombre`: `Sin estudios`
  - `Descripcion`: `CPTI Nivel Escolar Sin estudios`
  - `Habilitado`: `SI`

### `sispro_cpti_peligros_biologicos`  ·  10 filas  ·  7.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIPeligrosBiologicos>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:58Z  ·  sha256 `b8785ad55102…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CPTIPeligrosBiologicos`
  - `Codigo`: `1`
  - `Nombre`: `Contacto con animales o partes del sacrificio de los mismos`
  - `Descripcion`: `CPTI Peligros Biologicos`
  - `Habilitado`: `SI`

### `sispro_cpti_peligros_biomecanicos`  ·  5 filas  ·  3.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIPeligrosBiomecanicos>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:58Z  ·  sha256 `1acea5c5ea03…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CPTIPeligrosBiomecanicos`
  - `Codigo`: `1`
  - `Nombre`: `Exigencia de posturas o movimientos forzados`
  - `Descripcion`: `CPTI Peligros Biomecanicos`
  - `Habilitado`: `SI`

### `sispro_cpti_peligros_fisicos`  ·  8 filas  ·  5.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIPeligrosFisicos>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:59Z  ·  sha256 `7a636e112f66…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CPTIPeligrosFisicos`
  - `Codigo`: `1`
  - `Nombre`: `Presencia de ruido tan alto que no permite seguir una conversacion a un metro…`
  - `Descripcion`: `CPTI Peligro Fisico`
  - `Habilitado`: `SI`

### `sispro_cpti_peligros_psicosociales`  ·  10 filas  ·  7.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIPeligrosPsicosociales>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:15:59Z  ·  sha256 `b20365a81a56…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CPTIPeligrosPsicosociales`
  - `Codigo`: `1`
  - `Nombre`: `No es posible conversar y resolver los problemas fácilmente con los compañeros`
  - `Descripcion`: `CPTI Peligros Psicosociales`
  - `Habilitado`: `SI`

### `sispro_cpti_peligros_quimicos`  ·  5 filas  ·  3.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CPTIPeligrosQuimicos>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:00Z  ·  sha256 `d31fa8e06932…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CPTIPeligrosQuimicos`
  - `Codigo`: `1`
  - `Nombre`: `Exposición a humos o polvos en la realización de la tarea`
  - `Descripcion`: `CPTI Peligros Quimicos`
  - `Habilitado`: `SI`

### `sispro_ctr`  ·  23 filas  ·  14.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=CTR>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:00Z  ·  sha256 `14d369f60aee…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `CTR`
  - `Codigo`: `0`
  - `Nombre`: `Sin CTR Asignado`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_dci`  ·  10,000 filas  ·  5.6 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DCI>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:07Z  ·  sha256 `b40b414538e4…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `DCI`
  - `Codigo`: `1`
  - `Nombre`: `HIDRALAZINA`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_dis_rol_reportante`  ·  3 filas  ·  2.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DISRolReportante>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:07Z  ·  sha256 `49fb55f12405…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `DISRolReportante`
  - `Codigo`: `1`
  - `Nombre`: `Actor que fabrica o importa el dispositivo medico a reportar`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_dis_tipo_transaccion`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DISTipoTransaccion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:08Z  ·  sha256 `8d8b089a8cab…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `DISTipoTransaccion`
  - `Codigo`: `01`
  - `Nombre`: `Transaccion primaria`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_dispersion_geografica`  ·  5 filas  ·  3.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DispersionGeografica>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:08Z  ·  sha256 `7391f54db74e…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `DispersionGeografica`
  - `Codigo`: `1`
  - `Nombre`: `Dispersión alta`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_dmes_clasificacion_riesgo`  ·  4 filas  ·  2.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESClasificacionRiesgo>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:09Z  ·  sha256 `bdd12be26c9a…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `DMESClasificacionRiesgo`
  - `Codigo`: `1`
  - `Nombre`: `CLASE I`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_dmes_condicion_almacenamiento`  ·  12 filas  ·  7.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESCondicionAlmacenamiento>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:09Z  ·  sha256 `0f2f62d639fe…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `DMESCondicionAlmacenamiento`
  - `Codigo`: `1`
  - `Nombre`: `Temperatura menor o igual a 25° C`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_dmes_condicion_empaque`  ·  14 filas  ·  9.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESCondicionEmpaque>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:10Z  ·  sha256 `4d053e0796c2…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `DMESCondicionEmpaque`
  - `Codigo`: `1`
  - `Nombre`: `Temperatura menor o igual a 25° C`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_dmes_unidad_consumo`  ·  131 filas  ·  76.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=DMESUnidadConsumo>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:11Z  ·  sha256 `38bb02ccb3ab…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `DMESUnidadConsumo`
  - `Codigo`: `1`
  - `Nombre`: `AMPOLLA`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_eps_pm`  ·  110 filas  ·  66.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EPS_PM>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:11Z  ·  sha256 `1db730723677…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:CodEPS`, `Extra_II:NIT`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EPS_PM`
  - `Codigo`: `1`
  - `Nombre`: `COMFAMA`
  - `Descripcion`: ``
  - `Habilitado`: `NO`

### `sispro_eps_sy_liquidadas`  ·  78 filas  ·  46.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EPSSyLiquidadas>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:12Z  ·  sha256 `7edaa26ecc2a…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EPSSyLiquidadas`
  - `Codigo`: `CCF001`
  - `Nombre`: `COMFAMILIAR CAMACOL`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_epsc`  ·  55 filas  ·  35.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EPSC>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:13Z  ·  sha256 `afefec1ff0da…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:NIT`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EPSC`
  - `Codigo`: `CCFC07`
  - `Nombre`: `COMFAMILIAR CARTAGENA`
  - `Descripcion`: `Código aprobado por la Superintendencia Nacional de Salud`
  - `Habilitado`: `SI`

### `sispro_epss`  ·  55 filas  ·  35.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=EPSS>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:13Z  ·  sha256 `d8867ea7bde1…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:NIT`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `EPSS`
  - `Codigo`: `CCF002`
  - `Nombre`: `COMFAMA`
  - `Descripcion`: `Código aprobado por la Superintendencia Nacional de Salud`
  - `Habilitado`: `SI`

### `sispro_esquema_anexo_tecnico`  ·  237 filas  ·  225.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ESQUEMAAnexoTecnico>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:14Z  ·  sha256 `f0fb53019106…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Resolucion`, `Extra_II:CodVentana`, `Extra_III:IndPISISControlaCierrePeriodo`, `Extra_IV:EsArchivoPlano`
  `Extra_V:SeparadorCampos`, `Extra_VI:ExtensionesAceptables`, `Extra_VII:AreaUsuaria`, `Extra_VIII:EmailAreaUsuaria`, `Extra_IX:FormatoTransformacionTransporte`, `Extra_X:IndicadorTipoModuloNegocio`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ESQUEMAAnexoTecnico`
  - `Codigo`: `1477`
  - `Nombre`: `RIP155RIPS`
  - `Descripcion`: `RIP155RIPS - RIPS Atención comunidades Wuayuu`
  - `Habilitado`: `SI`

### `sispro_expresion_regular`  ·  106 filas  ·  78.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ExpresionRegular>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:15Z  ·  sha256 `466a645d8cd4…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II:Longitud`, `Extra_III:TipoDatoBasico.NetDB`, `Extra_IV:TipoDatoBasicoDB`
  `Extra_V:FormatoFecha.Net`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ExpresionRegular`
  - `Codigo`: `1`
  - `Nombre`: `TEXTO`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_ffm`  ·  47 filas  ·  50.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FFM>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:15Z  ·  sha256 `e1b9cfd41f0b…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:GrupoNivel1`, `Extra_II:GrupoNivel2`, `Extra_III:DefinicionGrupoNivel2`, `Extra_IV:GrupoNivel3`
  `Extra_V:DefinicionGrupoNivel3`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FFM`
  - `Codigo`: `C28944`
  - `Nombre`: `CREMA`
  - `Descripcion`: `Emulsión semisólida, generalmente con una proporción de 20% de agua y sustanc…`
  - `Habilitado`: `SI`

### `sispro_fne_direccion`  ·  121 filas  ·  70.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNEDireccion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:16Z  ·  sha256 `4749727b43b3…`
- **Columnas** (21):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Aplicación`, `Extra_II:Indicador`, `Extra_IV`, `Extra_V`
  `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`, `ValorRegistro`
  `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FNEDireccion`
  - `Codigo`: `1`
  - `Nombre`: `Anillo Vial`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_fne_link_validacion`  ·  7 filas  ·  5.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNELinkValidacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:17Z  ·  sha256 `d4ecbad4e156…`
- **Columnas** (21):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Aplicación`, `Extra_II:Link de Consulta`, `Extra_IV`, `Extra_V`
  `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`, `ValorRegistro`
  `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FNELinkValidacion`
  - `Codigo`: `1`
  - `Nombre`: `Rues`
  - `Descripcion`: `Registro Unico Empresarial`
  - `Habilitado`: `SI`

### `sispro_fne_listas_jife`  ·  11 filas  ·  7.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNEListasJife>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:17Z  ·  sha256 `c3a7970ebc02…`
- **Columnas** (20):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Aplicación`, `Extra_IV`, `Extra_V`, `Extra_VI`
  `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`, `ValorRegistro`, `UsuarioResponsable`
  `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FNEListasJife`
  - `Codigo`: `1`
  - `Nombre`: `LISTA AMARILLA (LISTA I)`
  - `Descripcion`: `Lista de estupefacientes`
  - `Habilitado`: `SI`

### `sispro_fne_modalidad_inscripcion`  ·  14 filas  ·  9.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNEModalidadInscripcion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:18Z  ·  sha256 `b2180c157a23…`
- **Columnas** (20):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Aplicación`, `Extra_IV`, `Extra_V`, `Extra_VI`
  `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`, `ValorRegistro`, `UsuarioResponsable`
  `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FNEModalidadInscripcion`
  - `Codigo`: `1`
  - `Nombre`: `Importación o compra local de sustancias para fabricar y vender medicamentos.`
  - `Descripcion`: `Art 26 o 28 Res 1478 de 2006`
  - `Habilitado`: `SI`

### `sispro_fne_naturaleza_juridica`  ·  7 filas  ·  4.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNENaturalezaJuridica>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:18Z  ·  sha256 `8c438e833f78…`
- **Columnas** (20):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Aplicación`, `Extra_IV`, `Extra_V`, `Extra_VI`
  `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`, `ValorRegistro`, `UsuarioResponsable`
  `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FNENaturalezaJuridica`
  - `Codigo`: `1`
  - `Nombre`: `Publica`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_fne_profesiones`  ·  28 filas  ·  16.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNEProfesiones>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:19Z  ·  sha256 `118b7978ecfb…`
- **Columnas** (20):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Aplicación`, `Extra_IV`, `Extra_V`, `Extra_VI`
  `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`, `ValorRegistro`, `UsuarioResponsable`
  `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FNEProfesiones`
  - `Codigo`: `1`
  - `Nombre`: `Abogado`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_fne_rol_tercero`  ·  7 filas  ·  4.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNERolTercero>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:19Z  ·  sha256 `b6edaaab0a19…`
- **Columnas** (20):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Aplicación`, `Extra_IV`, `Extra_V`, `Extra_VI`
  `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`, `ValorRegistro`, `UsuarioResponsable`
  `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FNERolTercero`
  - `Codigo`: `1`
  - `Nombre`: `Acondicionador`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_fne_tipo_proceso_act`  ·  17 filas  ·  10.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNETipoProcesoAct>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:20Z  ·  sha256 `751abda4c6c5…`
- **Columnas** (20):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Aplicación`, `Extra_IV`, `Extra_V`, `Extra_VI`
  `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`, `ValorRegistro`, `UsuarioResponsable`
  `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FNETipoProcesoAct`
  - `Codigo`: `1`
  - `Nombre`: `Importación`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_fne_tipo_producto_importar`  ·  3 filas  ·  2.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FNETipoProductoImportar>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:20Z  ·  sha256 `1713f846a880…`
- **Columnas** (20):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Aplicación`, `Extra_IV`, `Extra_V`, `Extra_VI`
  `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`, `ValorRegistro`, `UsuarioResponsable`
  `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FNETipoProductoImportar`
  - `Codigo`: `E`
  - `Nombre`: `Material de Referencia`
  - `Descripcion`: `Clasificación en solicitud de cupo Anexo 3`
  - `Habilitado`: `SI`

### `sispro_forma_comercializacion`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FormaComercializacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:21Z  ·  sha256 `00d557783597…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FormaComercializacion`
  - `Codigo`: `1`
  - `Nombre`: `NOMBRE COMUN`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_forma_contratacion_subsidiado`  ·  4 filas  ·  3.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FormaContratacionSubsidiado>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:21Z  ·  sha256 `d0fc3ed46549…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FormaContratacionSubsidiado`
  - `Codigo`: `1`
  - `Nombre`: `Capitación`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_franja`  ·  3 filas  ·  2.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Franja>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:22Z  ·  sha256 `2cfa76dc8138…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `Franja`
  - `Codigo`: `1`
  - `Nombre`: `VERDE`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_fuente_anexo_tecnico`  ·  65 filas  ·  41.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FUENTEAnexoTecnico>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:22Z  ·  sha256 `cfb960b39160…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FUENTEAnexoTecnico`
  - `Codigo`: `019`
  - `Nombre`: `Planilla integrada de liquidación de aportes PILA`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_fuente_financiacion`  ·  8 filas  ·  5.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=FuenteFinanciacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:23Z  ·  sha256 `d2c9cb0461e4…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `FuenteFinanciacion`
  - `Codigo`: `1`
  - `Nombre`: `Transferencias Nacionales`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_grupo_riesgo_capo`  ·  17 filas  ·  11.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=GrupoRiesgoCAPO>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:23Z  ·  sha256 `37fef155bf05…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `GrupoRiesgoCAPO`
  - `Codigo`: `000`
  - `Nombre`: `SIN GRUPO DE RIESGO CLASIFICADO`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_indicador_muestra_medica`  ·  9 filas  ·  6.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=IndicadorMuestraMedica>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:24Z  ·  sha256 `0cac86abdcc1…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `IndicadorMuestraMedica`
  - `Codigo`: `1`
  - `Nombre`: `GENERICO Y MARCA QUE NO ES MUESTRA MEDICA`
  - `Descripcion`: ``
  - `Habilitado`: `NO`

### `sispro_institucion_educacion_superior_snies`  ·  218 filas  ·  172.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=InstitucionEducacionSuperiorSNIES>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:25Z  ·  sha256 `e28ed8e35ea0…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:CodCaracterAcademico`, `Extra_II:CaracterAcademico`, `Extra_III:CodSector`, `Extra_IV:Sector`
  `Extra_V:CodDepartamento`, `Extra_VI:Departamento`, `Extra_VII:CodMunicipio`, `Extra_VIII:Municipio`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `InstitucionEducacionSuperiorSNIES`
  - `Codigo`: `1101`
  - `Nombre`: `UNIVERSIDAD NACIONAL DE COLOMBIA`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_institucion_formacion_trabajoy_desarrollo_humano_siet`  ·  716 filas  ·  516.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=InstitucionFormacionTrabajoyDesarrolloHumanoSIET>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:26Z  ·  sha256 `fee7e10e891b…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:CodDepartamento`, `Extra_II:Departamento`, `Extra_III:CodMunicipio`, `Extra_IV:Municipio`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `InstitucionFormacionTrabajoyDesarrolloHumanoSIET`
  - `Codigo`: `10045`
  - `Nombre`: `CLINICA SOMER`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_instituto_nacional_medicina_legal`  ·  332 filas  ·  218.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=InstitutoNacionalMedicinaLegal>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:27Z  ·  sha256 `3355334cdc1d…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `InstitutoNacionalMedicinaLegal`
  - `Codigo`: `05001INML33`
  - `Nombre`: `05001INML33 MEDELLIN`
  - `Descripcion`: `05001INML33 MEDELLIN`
  - `Habilitado`: `SI`

### `sispro_laboratorio_salud_publica`  ·  33 filas  ·  21.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LaboratorioSaludPublica>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:27Z  ·  sha256 `268a1f3d110b…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `LaboratorioSaludPublica`
  - `Codigo`: `05`
  - `Nombre`: `ENTIDAD TERRITORIAL DE ANTIOQUIA`
  - `Descripcion`: `ENTIDAD TERRITORIAL DE ANTIOQUIA`
  - `Habilitado`: `SI`

### `sispro_lc_elegible`  ·  3 filas  ·  2.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LCElegible>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:28Z  ·  sha256 `cacaddec8a97…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `LCElegible`
  - `Codigo`: `0`
  - `Nombre`: `Poblacion NO elegible para el régimen subsidiado`
  - `Descripcion`: `Poblacion Elegible para el subsidio en salud`
  - `Habilitado`: `SI`

### `sispro_lc_nuevo_estado`  ·  3 filas  ·  2.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=LCNuevoEstado>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:28Z  ·  sha256 `78bddefbbe2f…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `LCNuevoEstado`
  - `Codigo`: `0`
  - `Nombre`: `Activo`
  - `Descripcion`: `Estado Activo`
  - `Habilitado`: `SI`

### `sispro_min_salud_area_funcional`  ·  5 filas  ·  3.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=MinSaludAreaFuncional>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:29Z  ·  sha256 `280a905ac096…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `MinSaludAreaFuncional`
  - `Codigo`: `0`
  - `Nombre`: `Oficina de Promoción Social`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_pai_estado_fallecido`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PAIEstadoFallecido>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:29Z  ·  sha256 `c8b8e81b1ab5…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PAIEstadoFallecido`
  - `Codigo`: `1`
  - `Nombre`: `Activo`
  - `Descripcion`: `Activo`
  - `Habilitado`: `SI`

### `sispro_pais1`  ·  250 filas  ·  145.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Pais1>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:30Z  ·  sha256 `2b73690f62a6…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `Pais1`
  - `Codigo`: `004`
  - `Nombre`: `AFGANISTÁN`
  - `Descripcion`: `AFGANISTÁN`
  - `Habilitado`: `SI`

### `sispro_pase_componentes`  ·  12 filas  ·  8.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PASEComponentes>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:30Z  ·  sha256 `3956a2ed7063…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Orden`, `Extra_II:CodigoPASEDimension`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PASEComponentes`
  - `Codigo`: `1`
  - `Nombre`: `Tamaño`
  - `Descripcion`: `Tamaño`
  - `Habilitado`: `SI`

### `sispro_pase_dimension`  ·  5 filas  ·  3.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PASEDimension>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:31Z  ·  sha256 `2d2ca26ce3be…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Orden`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PASEDimension`
  - `Codigo`: `1`
  - `Nombre`: `Poblacional`
  - `Descripcion`: `Poblacional`
  - `Habilitado`: `SI`

### `sispro_pase_sub_componentes`  ·  41 filas  ·  29.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PASESubComponentes>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:32Z  ·  sha256 `c0cadd9952f0…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Orden`, `Extra_II:CodigoPASEDimension`, `Extra_III:CodigoPASEComponentes`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PASESubComponentes`
  - `Codigo`: `1`
  - `Nombre`: `Urbano`
  - `Descripcion`: `Urbano`
  - `Habilitado`: `SI`

### `sispro_pdsp_areas_observacion`  ·  71 filas  ·  53.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPAreasObservacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:32Z  ·  sha256 `81bcea511896…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Orden`, `Extra_II:Código PDSPDimension`, `Extra_III:Código PDSPComponente`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PDSPAreasObservacion`
  - `Codigo`: `1`
  - `Nombre`: `Acceso al agua potable y coberturas de acueducto, alcantarillado y aseo.`
  - `Descripcion`: `Acceso al agua potable y coberturas de acueducto, alcantarillado y aseo.`
  - `Habilitado`: `SI`

### `sispro_pdsp_categoria_fuente_financiacion`  ·  52 filas  ·  40.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPCategoriaFuenteFinanciacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:33Z  ·  sha256 `b9b2747e4435…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Orden`, `Extra_II:Código PDSPFuentesFinanciacion`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PDSPCategoriaFuenteFinanciacion`
  - `Codigo`: `1`
  - `Nombre`: `SGP - Salud Pública`
  - `Descripcion`: `SGP - Salud Pública`
  - `Habilitado`: `SI`

### `sispro_pdsp_categoria_linea_operativa`  ·  43 filas  ·  30.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPCategoriaLineaOperativa>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:33Z  ·  sha256 `eca76f16accc…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Orden`, `Extra_II:Código PDSPLineaOperativa`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PDSPCategoriaLineaOperativa`
  - `Codigo`: `1`
  - `Nombre`: `PIC - Rehabilitación basada en comunidad`
  - `Descripcion`: `PIC - Rehabilitación basada en comunidad`
  - `Habilitado`: `SI`

### `sispro_pdsp_componente`  ·  25 filas  ·  17.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPComponente>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:34Z  ·  sha256 `a6da71e85111…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Orden`, `Extra_II:Código PDSPDimension`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PDSPComponente`
  - `Codigo`: `1`
  - `Nombre`: `Hábitat saludable`
  - `Descripcion`: `Hábitat saludable`
  - `Habilitado`: `SI`

### `sispro_pdsp_dimension`  ·  10 filas  ·  7.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPDimension>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:34Z  ·  sha256 `bddc871408ed…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Orden`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PDSPDimension`
  - `Codigo`: `1`
  - `Nombre`: `Salud ambiental`
  - `Descripcion`: `Salud ambiental`
  - `Habilitado`: `SI`

### `sispro_pdsp_estrategias`  ·  417 filas  ·  592.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPEstrategias>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:36Z  ·  sha256 `04c848240973…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Orden`, `Extra_II:Código PDSPDimension`, `Extra_III:Código PDSPComponente`, `Extra_IV:Ámbito Nacional`
  `Extra_V:Ámbito Departamental`, `Extra_VI:Ámbito Distrital`, `Extra_VII:Ámbito Municipal`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PDSPEstrategias`
  - `Codigo`: `1`
  - `Nombre`: `Articulación interinstitucional para incorporar la salud ambiental en la form…`
  - `Descripcion`: `Articulación interinstitucional para incorporar la salud ambiental en la form…`
  - `Habilitado`: `SI`

### `sispro_pdsp_fuentes_financiacion`  ·  7 filas  ·  5.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PDSPFuentesFinanciacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:36Z  ·  sha256 `9758e69dff0b…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Orden`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PDSPFuentesFinanciacion`
  - `Codigo`: `1`
  - `Nombre`: `1. Recursos Provenientes del Sistema General de Participaciones (SGP), los es…`
  - `Descripcion`: `1. Recursos Provenientes del Sistema General de Participaciones (SGP), los es…`
  - `Habilitado`: `SI`

### `sispro_perfil_contratista`  ·  29 filas  ·  17.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PerfilContratista>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:37Z  ·  sha256 `4124de806d82…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PerfilContratista`
  - `Codigo`: `1`
  - `Nombre`: `Profesional en medicina`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_perfil_por_aplicacion`  ·  23 filas  ·  16.2 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PerfilPorAplicacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:37Z  ·  sha256 `f3d1808a1ce6…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:CodAplicacion`, `Extra_II:NombreAplicacion`, `Extra_III:TiposEntidad`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PerfilPorAplicacion`
  - `Codigo`: `1212`
  - `Nombre`: `THS Consulta Mesa Ayuda y Externos`
  - `Descripcion`: `THS Consulta Mesa Ayuda y Externos`
  - `Habilitado`: `SI`

### `sispro_ppss_eje_linea`  ·  33 filas  ·  24.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PPSSEjeLinea>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:38Z  ·  sha256 `e59c418528ee…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PPSSEjeLinea`
  - `Codigo`: `E1La`
  - `Nombre`: `DESTINAR Y GESTIONAR LOS RECURSOS FINANCIEROS NECESARIOS EN LOS PRESUPUESTOS …`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_ppss_poblacion_objetivo`  ·  26 filas  ·  16.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PPSSPoblacionObjetivo>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:38Z  ·  sha256 `e2d468f7a6a8…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PPSSPoblacionObjetivo`
  - `Codigo`: `01`
  - `Nombre`: `TRABAJADORES SECTOR SALUD`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_ppss_tipo_recurso`  ·  10 filas  ·  6.4 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PPSSTipoRecurso>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:16:39Z  ·  sha256 `44cf020a4cf5…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PPSSTipoRecurso`
  - `Codigo`: `01`
  - `Nombre`: `RECUROS PROPIOS DE LA ENTIDAD`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_precio_maximo_med_v2`  ·  78,000 filas  ·  64.3 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PrecioMaximoMED_V2>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:31Z  ·  sha256 `2f591ec81ac3…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:PMV_Transaccion`, `Extra_II:Margen_IPS`, `Extra_III:Circular_cnpmdm`, `Extra_IV:Fecha_inicio_vigencia`
  `Extra_V:Fecha_fin_vigencia`, `Extra_VI:Unidad_min_dispensacion`, `Extra_VII:PMV_unidad`, `Extra_VIII:PMV_unidad_margen`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PrecioMaximoMED_V2`
  - `Codigo`: `1`
  - `Nombre`: `VERAPAMILO - SOLIDO - ORAL`
  - `Descripcion`: `VERAPAMILO - SOLIDO - ORAL`
  - `Habilitado`: `SI`

### `sispro_pro170_causa_levan`  ·  4 filas  ·  3.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PRO170CausaLevan>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:32Z  ·  sha256 `b036199b4a7c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PRO170CausaLevan`
  - `Codigo`: `1`
  - `Nombre`: `INASISTENCIA INJUSTIFICADA CITAS`
  - `Descripcion`: `INASISTENCIA INJUSTIFICADA CITAS`
  - `Habilitado`: `SI`

### `sispro_pro170_fase_implementacion`  ·  4 filas  ·  3.0 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PRO170FaseImplementacion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:32Z  ·  sha256 `092ab4173e15…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PRO170FaseImplementacion`
  - `Codigo`: `1`
  - `Nombre`: `OTORGADA`
  - `Descripcion`: `OTORGADA`
  - `Habilitado`: `SI`

### `sispro_pro170_tipo_beneficiario`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PRO170TipoBeneficiario>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:33Z  ·  sha256 `5e88cae1e108…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PRO170TipoBeneficiario`
  - `Codigo`: `1`
  - `Nombre`: `Mujer`
  - `Descripcion`: `Mujer`
  - `Habilitado`: `SI`

### `sispro_pro170_tipo_medida`  ·  3 filas  ·  2.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PRO170TipoMedida>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:33Z  ·  sha256 `c649d9cd145c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PRO170TipoMedida`
  - `Codigo`: `1`
  - `Nombre`: `HABITACION ALIMENTACION CASA ALBERGUE`
  - `Descripcion`: `HABITACION ALIMENTACION CASA ALBERGUE`
  - `Habilitado`: `SI`

### `sispro_programa_educacion_siet`  ·  4,000 filas  ·  3.3 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ProgramaEducacionSIET>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:35Z  ·  sha256 `1ac48469ea12…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Cod NucleoBasico`, `Extra_II:NucleoBasico`, `Extra_III:CodTipoCertificado`, `Extra_IV:TipoCertificado`
  `Extra_V:CodModalidadMetodologia`, `Extra_VI:ModalidadMetodologia`, `Extra_VII:CodDepartamento`, `Extra_VIII:Departamento`, `Extra_IX:CodMunicipio`, `Extra_X:Municipio`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ProgramaEducacionSIET`
  - `Codigo`: `100`
  - `Nombre`: `TECNICO LABORAL POR COMPETENCIAS EN AUXILIAR EN ENFERMERIA`
  - `Descripcion`: ``
  - `Habilitado`: `NO`

### `sispro_programa_educacion_superior_snies`  ·  4,000 filas  ·  3.3 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ProgramaEducacionSuperiorSNIES>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:38Z  ·  sha256 `98c3e2081dfb…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:CodNucleoBasico`, `Extra_II:NucleoBasico`, `Extra_III:CodNivelFormacion`, `Extra_IV:NivelFormacion`
  `Extra_V:CodModalidadMetodologia`, `Extra_VI:ModalidadMetodologia`, `Extra_VII:CodDepartamento`, `Extra_VIII:Departamento`, `Extra_IX:CodMunicipio`, `Extra_X:Municipio`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ProgramaEducacionSuperiorSNIES`
  - `Codigo`: `10`
  - `Nombre`: `NUTRICION Y DIETETICA`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_pss_excepcion`  ·  54 filas  ·  45.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=PSSExcepcion>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:39Z  ·  sha256 `92b331e2c9ae…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Telefono`, `Extra_II:Gerente`, `Extra_III:Regimen`, `Extra_IV:CodDepartamento`
  `Extra_V:Departamento`, `Extra_VI:CodMunicipio`, `Extra_VII:Municipio`, `Extra_VIII:Email`, `Extra_IX:NITDigito`, `Extra_X:NIT`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `PSSExcepcion`
  - `Codigo`: `050018800101`
  - `Nombre`: `MARIA ELISA MEJIA`
  - `Descripcion`: `Carrera 43 No. 29 -35 Consultorio 705`
  - `Habilitado`: `SI`

### `sispro_resguardo_nit`  ·  13 filas  ·  8.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=ResguardoNit>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:39Z  ·  sha256 `61256bec2be9…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `ResguardoNit`
  - `Codigo`: `80021786`
  - `Nombre`: `resguardo indigena de muellamues`
  - `Descripcion`: `resguardo indigena de muellamues`
  - `Habilitado`: `SI`

### `sispro_sac_etapa_proceso`  ·  9 filas  ·  5.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACEtapaProceso>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:40Z  ·  sha256 `fe81c76f4883…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SACEtapaProceso`
  - `Codigo`: `0`
  - `Nombre`: `0.No esta en proceso jurídico`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_sac_mecanismo_calculo`  ·  2 filas  ·  1.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACMecanismoCalculo>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:40Z  ·  sha256 `e266690915a4…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SACMecanismoCalculo`
  - `Codigo`: `CA`
  - `Nombre`: `Comparador Administrativo`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_sac_origen_cobro`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACOrigenCobro>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:41Z  ·  sha256 `019691a11f58…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SACOrigenCobro`
  - `Codigo`: `CTC`
  - `Nombre`: `Comité Técnico Científico`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_sac_tipo_cobro`  ·  2 filas  ·  1.7 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACTipoCobro>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:42Z  ·  sha256 `567cbb1d0e7f…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SACTipoCobro`
  - `Codigo`: `F`
  - `Nombre`: `Factura`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_sac_tipo_servicio`  ·  4 filas  ·  2.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SACTipoServicio>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:42Z  ·  sha256 `8eda9f82c0b6…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SACTipoServicio`
  - `Codigo`: `1`
  - `Nombre`: `Medicamento`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_seg_materna_tipo_caso`  ·  13 filas  ·  8.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SegMaternaTipoCaso>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:43Z  ·  sha256 `e0312bba6c50…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SegMaternaTipoCaso`
  - `Codigo`: `1`
  - `Nombre`: `Mayor de 35 años`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_ser_acto_admin_ejec`  ·  7 filas  ·  4.6 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SERActoAdminEjec>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:43Z  ·  sha256 `afcc0bfe1a8c…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SERActoAdminEjec`
  - `Codigo`: `1`
  - `Nombre`: `Contrato`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_ser_acto_admin_incorp`  ·  5 filas  ·  3.5 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SERActoAdminIncorp>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:44Z  ·  sha256 `f6bf4dfff1dd…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SERActoAdminIncorp`
  - `Codigo`: `1`
  - `Nombre`: `Ordenanza`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_serid_recurso`  ·  14,000 filas  ·  9.7 MB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SERIDRecurso>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:54Z  ·  sha256 `56df4486f195…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SERIDRecurso`
  - `Codigo`: `ID0019621301`
  - `Nombre`: `Prom Social RES 0196 DEPARTAMENTO DE ANTIOQUIA_INIMPUTABLES`
  - `Descripcion`: `SD`
  - `Habilitado`: `SI`

### `sispro_si_no_pensionado`  ·  3 filas  ·  2.3 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SiNoPensionado>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:54Z  ·  sha256 `b1db1636f006…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:SiNoPensionado`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SiNoPensionado`
  - `Codigo`: `1`
  - `Nombre`: `Si`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_suf_comodin1`  ·  1 filas  ·  1.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SUFComodin1>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:55Z  ·  sha256 `0b5df4c66e84…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SUFComodin1`
  - `Codigo`: `AXX`
  - `Nombre`: `Comodín estudio suficiencia`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_suf_insumos_lentes_monturas_sten`  ·  19 filas  ·  12.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=SUFInsumosLentesMonturasSten>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:55Z  ·  sha256 `b813d8582b47…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `SUFInsumosLentesMonturasSten`
  - `Codigo`: `170100`
  - `Nombre`: `Lentes`
  - `Descripcion`: `Lentes`
  - `Habilitado`: `SI`

### `sispro_tv_tipo_receptor`  ·  13 filas  ·  8.8 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TVTipoReceptor>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:56Z  ·  sha256 `9924a17789b0…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TVTipoReceptor`
  - `Codigo`: `1`
  - `Nombre`: `Prescriptores de servicios, productos farmaceuticos y tecnologias en salud`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_tv_tipo_transferencia`  ·  11 filas  ·  7.9 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=TVTipoTransferencia>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:56Z  ·  sha256 `27b2a9d8f60e…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `TVTipoTransferencia`
  - `Codigo`: `1`
  - `Nombre`: `Entrega y/o pago de alimentacion y bebidas`
  - `Descripcion`: ``
  - `Habilitado`: `SI`

### `sispro_umm`  ·  273 filas  ·  166.1 KB

- **Kind**: `sispro_aspx`
- **URL**: <https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=UMM>
- **Licencia**: MinSalud SISPRO — uso público
- **Versión / sync**: 2026-05-02T21:17:57Z  ·  sha256 `526e02ca37ca…`
- **Columnas** (22):
  `Tabla`, `Codigo`, `Nombre`, `Descripcion`, `Habilitado`, `Aplicacion`
  `IsStandardGEL`, `IsStandardMSPS`, `Extra_I:Simbolo UMM`, `Extra_II`, `Extra_III`, `Extra_IV`
  `Extra_V`, `Extra_VI`, `Extra_VII`, `Extra_VIII`, `Extra_IX`, `Extra_X`
  `ValorRegistro`, `UsuarioResponsable`, `Fecha_Actualizacion`, `IsPublicPrivate`
- **Ejemplo (fila 0, primeros 5 campos)**:
  - `Tabla`: `UMM`
  - `Codigo`: `1`
  - `Nombre`: `EID50`
  - `Descripcion`: `dosis infecciosa de embrión 50`
  - `Habilitado`: `SI`


---

## Totales

- **319 catálogos**
- **2,524,483 filas** sincronizadas
- **3.0 GB** total en disco
